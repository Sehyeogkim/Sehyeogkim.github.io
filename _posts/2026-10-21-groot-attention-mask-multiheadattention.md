---
layout: post
title: "GR00T N1.7 Attention Mask - PyTorch MultiheadAttention"
date: 2026-10-21 16:00:00 +0900
categories: [Study, Robotics]
section: Study
study_area: Robotics
topic: "VLA"
tags: [vla, gr00t, attention-mask, multiheadattention, pytorch, key-padding-mask, sdpa, smolvla]
description: "torch.nn.MultiheadAttention 안에서 key_padding_mask 와 attn_mask 가 _canonical_mask → 합치기 → SDPA 로 어떻게 처리되는지 실제 코드로 따라가고, bool 의미가 함수마다 반대인 함정과 SmolVLA(causal) vs GR00T(양방향) action mask 설계를 비교한다."
permalink: /blog/robotics/vla/groot-attention-mask-multiheadattention/
media_subpath: /blog/robotics/vla/groot-attention-mask-multiheadattention/
---

> 이번시간에는 torch → nn → modules → `activation.py` 에 적힌 MultiheadAttention class → forward 에서 정확하게 attention mask 가 어떻게 생성되고, 적용되는지를 살펴보자.
{: .prompt-info }

<div class="notion-gap" style="--gap: 1"></div>

출발점은 GR00T N1.7 code scratch part1 에서 짠 DiT 블록이다. self / cross attention 둘 다 `torch.nn.MultiheadAttention` 에 맡겼었는데, 그 안에서 mask 가 어떻게 처리되는지 오늘 제대로 뜯어보자.

<div class="notion-gap" style="--gap: 1"></div>

```py
class _DiTBlock(torch.nn.Module):
    '''self-attn(state+action) 다음에 VLM hidden 으로 cross-attn. 시간은 AdaLN.'''

    def __init__(self, dim, heads, cross_dim, ffn_dim):
        super().__init__()
        self.adaln_self = _AdaLN(dim, dim)
        self.adaln_cross = _AdaLN(dim, dim)
        self.adaln_ff = _AdaLN(dim, dim)
        self.self_attn = torch.nn.MultiheadAttention(dim, heads, batch_first=True)
        self.cross_attn = torch.nn.MultiheadAttention(
            dim, heads, kdim=cross_dim, vdim=cross_dim, batch_first=True
        )
        self.ff = torch.nn.Sequential(
            torch.nn.Linear(dim, ffn_dim),
            torch.nn.GELU(),
            torch.nn.Linear(ffn_dim, dim),
        )

    def forward(self, x, context, cond, context_pad):
        '''
            context - Normed hidden state from VLM.
            cond    - Denoising time condition.
        '''
        h = self.adaln_self(x, cond)
        h = self.self_attn(h, h, h, need_weights=False)[0] + x
        y = self.adaln_cross(h, cond)
        y = self.cross_attn(
            y, context, context, key_padding_mask=~context_pad, need_weights=False
        )[0] + h
        return self.ff(self.adaln_ff(y, cond)) + y
```

<div class="notion-gap" style="--gap: 2"></div>

여기서 이제 MultiHeadAttention class를 먼저 살펴보자. 살펴보면 key padding mask 와 attn\_mask가 보일 것이다.

```py
class MultiheadAttention(Module):
    def forward(
        self,
        query: Tensor,
        key: Tensor,
        value: Tensor,
        key_padding_mask: Tensor | None = None,
        need_weights: bool = True,
        attn_mask: Tensor | None = None,
        average_attn_weights: bool = True,
        is_causal: bool = False,
    ) -> tuple[Tensor, Tensor | None]:
```

<div class="notion-gap" style="--gap: 2"></div>

```py
key_padding_mask = F._canonical_mask(
    mask=key_padding_mask,
    mask_name="key_padding_mask",
    other_type=F._none_or_dtype(attn_mask),
    other_name="attn_mask",
    target_type=query.dtype,
)

attn_mask = F._canonical_mask(
    mask=attn_mask,
    mask_name="attn_mask",
    other_type=None,
    other_name="",
    target_type=query.dtype,
    check_other=False,
)
```

위에서 보면 mask 가 두 종류다. 헷갈리니까 먼저 정리하고 가자.

|  | `key_padding_mask` | `attn_mask` |
|---|---|---|
| 모양 | `[B, S]` (key 토큰마다 1 개) | `[L, S]` 또는 `[B·H, L, S]` (query × key 칸마다 1 개) |
| 뜻 | "이 **key 토큰**은 pad 니까 **아무도** 보지 마" | "이 **query** 는 이 **key** 를 보지 마" (causal 같은 규칙) |
| 우리 DiT 에서 | cross-attn 에 `~context_pad` | 안 씀 (self-attn 은 mask 없음) |
| bool 일 때 True | **True = 가림** | **True = 가림** |

<div class="notion-gap" style="--gap: 1"></div>

그리고 이 둘은 결국 **하나로 합쳐져서** 마지막에 score 에 더해진다. 순서대로 따라가보자.

<div class="notion-gap" style="--gap: 1"></div>

### 1. `_canonical_mask`: bool → 더할 값 (-inf)

---

위에서 두 mask 다 제일 먼저 `F._canonical_mask` 를 통과한다. `torch/nn/functional.py` 에 있는 진짜 코드를 열어보면 생각보다 단순하다.

```py
def _canonical_mask(mask, mask_name, other_type, other_name, target_type, check_other=True):
    if mask is not None:
        _mask_dtype = mask.dtype
        _mask_is_float = torch.is_floating_point(mask)
        if _mask_dtype != torch.bool and not _mask_is_float:
            raise AssertionError(f"only bool and floating types of {mask_name} are supported")
        ...
        if not _mask_is_float:
            mask = torch.zeros_like(mask, dtype=target_type).masked_fill_(
                mask, float("-inf")
            )
    return mask
```

- 핵심은 마지막 두 줄. **bool 이면 0 으로 채운 float 텐서를 만들고, True 자리만 -inf** 로 바꾼다.
- 즉 "가릴까 말까" (bool) 를 "score 에 **더할 값**" (0 / -inf) 으로 번역하는 함수다. 내 SmolVLA 구조 코드에서 우리가 `torch.where(mask, 0.0, finfo.min)` 으로 직접 했던 거랑 똑같은 일을 torch 가 해주는 것.
- float 로 넘기면 아무것도 안 하고 그대로 쓴다 (이미 "더할 값" 이라고 보는 것).

<div class="notion-gap" style="--gap: 1"></div>

직접 돌려보면:

```py
kpm = torch.tensor([[False, False, False, True, True]])   # True = pad (가릴 칸)
F._canonical_mask(mask=kpm, mask_name="kpm", other_type=None, other_name="", target_type=torch.float32)
# tensor([[0., 0., 0., -inf, -inf]])
```

<div class="notion-gap" style="--gap: 1"></div>

### 2. key\_padding\_mask 를 attn\_mask 에 합치기

---

그 다음 실제 계산은 `F.multi_head_attention_forward` 로 넘어간다. 여기서 q, k, v 를 head 로 쪼개고 나서, 두 mask 를 **하나로 합친다**.

```py
# merge key padding and attention masks
if key_padding_mask is not None:
    _check_key_padding_mask(key_padding_mask, src_len, bsz)     # [B, S] 모양인지 검사

    key_padding_mask = (
        key_padding_mask.view(bsz, 1, 1, src_len)               # [B, 1, 1, S]
        .expand(-1, num_heads, -1, -1)                          # [B, H, 1, S]  head 마다 복사
        .reshape(bsz * num_heads, 1, src_len)                   # [B·H, 1, S]
    )
    if attn_mask is None:
        attn_mask = key_padding_mask                            # attn_mask 없으면 그대로
    else:
        attn_mask = attn_mask + key_padding_mask                # 있으면 더하기 (-inf + 0 = -inf)
```

- `key_padding_mask` 는 원래 `[B, S]` 라서 **query 축 (L) 이 없다.** 그래서 `[B·H, 1, S]` 로 만들어두면, 나중에 `[B·H, L, S]` 와 더할 때 **L 방향으로 broadcast** 된다. → query 가 몇 개든 전부 **같은 칸 (pad) 을 가린다.**
- 둘 다 이미 0 / -inf 라서 합치는 건 그냥 **덧셈**. 한쪽이라도 -inf 면 결과도 -inf.
- 재밌는 건 head 마다 복사한다는 것. pad 는 head 랑 상관없으니까 9 개든 32 개든 다 같은 mask.

<div class="notion-gap" style="--gap: 1"></div>

### 3. scaled\_dot\_product\_attention: score 에 더하고 softmax

---

마지막에 합쳐진 mask 를 `[B, H, L, S]` 로 펴서 `scaled_dot_product_attention` 에 넘긴다. 이 함수가 내부에서 하는 일을 torch 문서에 적힌 **참고용 파이썬 구현**으로 보면 이렇다.

```py
def scaled_dot_product_attention(query, key, value, attn_mask=None, dropout_p=0.0, is_causal=False, scale=None):
    L, S = query.size(-2), key.size(-2)
    scale_factor = 1 / math.sqrt(query.size(-1)) if scale is None else scale
    attn_bias = torch.zeros(L, S, dtype=query.dtype, device=query.device)
    if is_causal:
        temp_mask = torch.ones(L, S, dtype=torch.bool).tril(diagonal=0)
        attn_bias.masked_fill_(temp_mask.logical_not(), float("-inf"))
    if attn_mask is not None:
        if attn_mask.dtype == torch.bool:
            attn_bias.masked_fill_(attn_mask.logical_not(), float("-inf"))   # <- 주의: 여기선 True = 봄
        else:
            attn_bias = attn_mask + attn_bias

    attn_weight = query @ key.transpose(-2, -1) * scale_factor   # [B, H, L, S]
    attn_weight += attn_bias                                      # <- mask 는 softmax 전에 더한다
    attn_weight = torch.softmax(attn_weight, dim=-1)
    return attn_weight @ value
```

- 우리가 직접 짰던 `scores.masked_fill(...)` → `softmax` 랑 **완전히 같은 순서**다. mask 는 무조건 **softmax 전에**.
- -inf 칸은 exp(-inf) = 0 이라서 softmax 후 **정확히 0** 이 된다.

<div class="notion-gap" style="--gap: 1"></div>

한눈에 보면 이런 흐름이다.

![](images/img-001.png)

<div class="notion-gap" style="--gap: 1"></div>

#### 실제로 확인해보자

---

query 3 개, key 5 개 (마지막 2 개가 pad) 로 `nn.MultiheadAttention` 을 직접 돌려봤다.

```py
mha = torch.nn.MultiheadAttention(8, 2, batch_first=True)
q = torch.randn(1, 3, 8); kv = torch.randn(1, 5, 8)
kpm = torch.tensor([[False, False, False, True, True]])

out, w = mha(q, kv, kv, key_padding_mask=kpm, need_weights=True, average_attn_weights=False)
print(w[0, 0])     # head 0 의 attention 가중치
# tensor([[0.0930, 0.6960, 0.2110, 0.0000, 0.0000],
#         [0.3510, 0.2630, 0.3860, 0.0000, 0.0000],
#         [0.2320, 0.2270, 0.5410, 0.0000, 0.0000]])

# pad 자리 내용을 아무렇게나 바꿔도?
kv2 = kv.clone(); kv2[:, 3:] = 100 * torch.randn(1, 2, 8)
out2, _ = mha(q, kv2, kv2, key_padding_mask=kpm, need_weights=False)
torch.allclose(out, out2)    # True  -> pad 는 출력에 아무 영향이 없다
```

- 3 개 query 전부 pad 2 칸이 **정확히 0**. 그리고 나머지 3 칸끼리 합이 1.
- pad 자리에 100 배짜리 쓰레기 값을 넣어도 출력이 똑같다. 이게 "가린다" 의 진짜 의미.

<div class="notion-gap" style="--gap: 1"></div>

### 4. 제일 헷갈렸던 것: bool 의 의미가 함수마다 반대다

---

> - `nn.MultiheadAttention` 의 `key_padding_mask` / `attn_mask` : **True = 가림**
> - `F.scaled_dot_product_attention` 의 bool `attn_mask` : **True = 봄** (`attn_mask.logical_not()` 으로 뒤집어서 -inf)
> - 내 SmolVLA 구조 코드의 `make_att_2d_masks` 결과 : **True = 봄** (그래서 `masked_fill(attn_mask == False, -1e9)` 로 썼다)
{: .prompt-info }

그래서 GR00T DiT 에서 `key_padding_mask=~context_pad` 로 `~` (뒤집기) 를 붙인 거다.

- `context_pad` 는 VLM processor 가 준 `attention_mask` 를 bool 로 바꾼 것 → **True = 진짜 토큰**
- MultiheadAttention 은 **True = 가림** 을 원하니까 → `~` 로 뒤집어서 넘긴다.
- 만약 `~` 를 빼먹으면? **진짜 토큰을 전부 가리고 pad 만 보게** 된다. 에러도 안 나고 조용히 학습이 망가진다. (제일 무서운 버그 유형)

<div class="notion-gap" style="--gap: 1"></div>

### 5. 우리 DiT 블록에 대입하면

---

```py
h = self.self_attn(h, h, h, need_weights=False)[0] + x                       # mask 없음
y = self.cross_attn(y, context, context, key_padding_mask=~context_pad, ...)  # pad 만 가림
```

- **self-attn (state 1 + action 40 = 41 토큰)**: mask 를 아무것도 안 넘겼다 → `attn_mask = None` → 41 개 토큰이 **서로 전부 본다 (양방향)**.
- **cross-attn (41 토큰 → VLM hidden S 개)**: `key_padding_mask` 만 → VLM 쪽 pad 토큰만 가린다. `[B, S]` → `[B·H, 1, S]` → 41 개 query 전부에 broadcast.
- causal 을 쓰고 싶으면 `attn_mask` 에 위삼각 bool 을 넘기면 된다. 직접 해보면 이렇게 나온다.

```py
L = 4
causal = torch.triu(torch.ones(L, L, dtype=torch.bool), 1)   # True = 가림 (자기보다 뒤)
# [[0, 1, 1, 1],
#  [0, 0, 1, 1],
#  [0, 0, 0, 1],
#  [0, 0, 0, 0]]
_, w = sa(x, x, x, attn_mask=causal, need_weights=True)
# [[1.00, 0.00, 0.00, 0.00],
#  [0.33, 0.67, 0.00, 0.00],
#  [0.35, 0.30, 0.34, 0.00],
#  [0.27, 0.24, 0.22, 0.27]]    <- 하삼각만 남는다
```

<div class="notion-gap" style="--gap: 1"></div>

## 내 SmolVLA 구조 vs GR00T: action 은 무엇을 볼 수 있나

---

여기서 하나 궁금했던 게 있다. 내 SmolVLA 구조 코드에서는 action 끼리 **causal** 로 가렸는데, GR00T 는 self-attn 에 mask 를 아예 안 준다. 둘 중 뭐가 맞는 걸까?

![](images/img-002.png)

|  | 내 코드 / SmolVLA | GR00T N1.7 |
|---|---|---|
| mask 를 누가 만드나 | 내가 직접 (`make_att_2d_masks` → 2D → `masked_fill`) | torch 가 (`key_padding_mask` → -inf → `[B·H, L, S]`) |
| self layer: action 끼리 | **causal** (앞 action 만 봄) | **양방향** (mask 없음) |
| self layer: 관측 (prefix) | KV cache 413 을 같이 봄 (pad 7 가림) | 안 봄 (state + action 41 개끼리만) |
| cross layer | prefix 413 만 봄 (pad 가림) | VLM hidden 만 봄 (pad 가림) |
| self / cross 배치 | layer 마다 번갈아 (짝수 self, 홀수 cross) | 내 코드: 한 블록 안에 둘 다 / 공식 AlternateVLDiT: 블록 단위로 번갈아 |

<div class="notion-gap" style="--gap: 1"></div>

**결론: 둘 다 맞다. 버그가 아니라 설계 선택이다.**

- `causal mask` 는 원래 **"정답 훔쳐보기" 를 막으려고** 있는 것이다. VLM 학습 (teacher forcing) 에서는 입력에 정답 토큰이 그대로 들어가니까 뒤를 보면 답을 베낀다.
- 그런데 flow matching 은 입력이 40 칸 전부 **noise 섞인 x\_t** 다. 정답 (깨끗한 action) 은 입력 어디에도 없다. 옆 칸을 봐도 "다른 칸의 noisy 버전" 뿐이라 **베낄 답이 없다.**
- 그리고 추론할 때도 40 칸을 **동시에** 다듬는다 (GPT 처럼 하나씩 생성하지 않는다). 그러니까 양방향으로 서로 보면서 "1 번이 오른쪽으로 가니까 2 번도 부드럽게 이어서" 처럼 **chunk 전체를 일관되게** 맞추는 게 자연스럽다.
- 그래서 `π0, GR00T, Diffusion Policy 는 action 끼리 양방향`이고, `SmolVLA 는 causal` 을 골랐다. 내 코드는 SmolVLA 를 따라서 causal 이었던 것. 학습과 추론에 같은 mask 를 썼으니까 틀린 건 아니다.

<div class="notion-gap" style="--gap: 1"></div>

궁금하면 내 코드에서 한 줄만 바꿔서 실험해볼 수 있다.

```py
# suffix_att_mask = torch.ones(B, 16)                              # SmolVLA: action 끼리 causal
suffix_att_mask = torch.zeros(B, 16); suffix_att_mask[:, 0] = 1    # π0: action 블록 안에서 양방향
```

첫 칸만 1 이라서 "action 블록이 새로 시작" (prefix 는 action 을 못 봄) 은 그대로고, 블록 안에서는 서로 다 본다. 지금 66% 짜리 모델 (crop + EMA) 이랑 같은 조건으로 돌려서 비교해볼 예정.

<div class="notion-gap" style="--gap: 1"></div>

## Summary

---

- `nn.MultiheadAttention` 의 mask 는 결국 **"score 에 더할 값" 하나**로 합쳐진다. bool → `_canonical_mask` (True → -inf) → `key_padding_mask` 는 `[B·H, 1, S]` 로 펴서 `attn_mask` 에 더하기 → softmax 전에 score 에 더하기.
- `key_padding_mask` 는 "이 key 는 아무도 보지 마" (pad), `attn_mask` 는 "이 query 는 이 key 를 보지 마" (causal 같은 규칙). 앞의 것은 query 축으로 broadcast 된다.
- **bool 의 의미가 함수마다 반대다.** MultiheadAttention 은 True = 가림, SDPA 는 True = 봄. 그래서 `~context_pad`. 이거 하나 틀리면 에러 없이 조용히 망가진다.
- GR00T DiT 는 self-attn 에 mask 가 없다 (action 끼리 양방향), cross-attn 은 VLM pad 만 가린다. 내 코드 (SmolVLA 식) 는 action 끼리 causal. flow matching 에서는 베낄 정답이 없어서 **둘 다 성립**하는 설계 선택이다.

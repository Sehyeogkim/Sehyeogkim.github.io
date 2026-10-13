---
layout: post
title: "Attention Mask"
date: 2026-10-13 10:30:00 +0900
categories: [Study, Robotics]
section: Study
study_area: Robotics
topic: "VLA"
tags: [vla, attention-mask, causal-mask, prefix-lm, smolvla, lerobot, transformer]
description: "앞으로 죽도록 들을 Attention Mask를 한번 정리한다. 용도(패딩, causal, VLA 블록 규칙), 1D pad/att mask를 cumsum으로 2D로 만드는 make_att_2d_masks, 그리고 softmax 직전에 어떻게 쓰이는지까지 SmolVLA 코드로 확인한다."
permalink: /blog/robotics/vla/attention-mask/
media_subpath: /blog/robotics/vla/attention-mask/
math: true
---

Attention Mask라는 개념을 이제 사실 죽도록 들을 것이기 때문에, 이 시간에는 한번 정리를 해보자 정확하게 용도는 무엇이며 코드로 어떻게 생성하고 사용하는지.

<div class="notion-gap" style="--gap: 1"></div>

## Contents

---

- 용도
- 생성 코드
- 사용 코드

<div class="notion-gap" style="--gap: 1"></div>

## Purpose

---

일단 어텐션의 핵심은 Query, Key, Value이다.

즉 내가 다음 토큰을 예측할때, 결국에 이전 토큰들을 참고하고 어느정도 참고해야할 지를 학습하는 것이다. 그렇다면 참고해야할 토큰이 있고 아닌 토큰이 있는 경우가 발생한다.

<div class="notion-gap" style="--gap: 1"></div>

예를들어보자,

![](images/img-001.png)

**1) 패딩 토큰**

문장 길이를 48로 맞추려고 뒤에 채워 넣은 빈칸(pad)이다. 아무 의미도 없는 토큰이니까 누구도 참고하면 안 된다.

<div class="notion-gap" style="--gap: 1"></div>

**2) 미래 토큰 (GPT)**

다음 토큰을 예측하는데 이미 정답(미래 토큰)을 볼 수 있으면? 그냥 커닝이다 ㅋㅋ 그래서 나보다 뒤에 있는 토큰은 못 보게 막아야 한다. 이게 바로 **Causal Mask**.

<div class="notion-gap" style="--gap: 1"></div>

**3) VLA (SmolVLA)**

여기서 좀 재밌어진다. 블록마다 규칙이 다르다.

- image + language: 관측끼리는 서로 다 봐야 한다 (full)
- state: 관측은 볼 수 있지만, 관측은 state를 못 본다 (새 블록)
- action: 관측을 전부 봐야 한다. 하지만 관측은 action을 보면 안 된다 → 추론 때 prefix를 액션 없이 먼저 돌려서 KV cache로 만들어두기 때문에, 학습 때도 똑같이 막아줘야 한다.

> 결국 Attention Mask = **"누가(query i) → 누구를(key j) 볼 수 있는가"** 를 적어둔 `[L, L]` 표이다.<br>1 = 볼 수 있음, 0 = 못 봄. 행이 query, 열이 key.
{: .prompt-info }

실제로 SmolVLA prefix(241개 토큰)의 mask를 뽑아보면 다음과 같다. (흰색 = 볼 수 있음)

![](images/img-002.png)

- 왼쪽 위 큰 흰 사각형: image + language끼리 full attention
- 검은 띠: language padding (행도 열도 전부 0)
- 맨 아래 한 줄(state): 앞의 관측은 다 보지만, 위의 관측 행들은 state 열을 못 본다

<div class="notion-gap" style="--gap: 3"></div>

## make_att_2d_masks

---

```python
def make_att_2d_masks(pad_masks: Tensor, att_masks: Tensor) -> Tensor:  # see openpi (exact copy)
    """Copied from big_vision.

    Tokens can attend to valid inputs tokens which have a cumulative mask_ar
    smaller or equal to theirs. This way `mask_ar` int[B, N] can be used to
    setup several types of attention, for example:

      [[1 1 1 1 1 1]]: pure causal attention.

      [[0 0 0 1 1 1]]: prefix-lm attention. The first 3 tokens can attend between
          themselves and the last 3 tokens have a causal attention. The first
          entry could also be a 1 without changing behaviour.

      [[1 0 1 0 1 0 0 1 0 0]]: causal attention between 4 blocks. Tokens of a
          block can attend all previous blocks and all tokens on the same block.

    Args:
      input_mask: bool[B, N] true if its part of the input, false if padding.
      mask_ar: int32[B, N] mask that's 1 where previous tokens cannot depend on
        it and 0 where it shares the same attention mask as the previous token.
    """
    if att_masks.ndim != 2:
        raise ValueError(att_masks.ndim)
    if pad_masks.ndim != 2:
        raise ValueError(pad_masks.ndim)

    cumsum = torch.cumsum(att_masks, dim=1)
    att_2d_masks = cumsum[:, None, :] <= cumsum[:, :, None]
    pad_2d_masks = pad_masks[:, None, :] * pad_masks[:, :, None]
    return att_2d_masks & pad_2d_masks
```

<div class="notion-gap" style="--gap: 1"></div>

생각보다 코드는 단순하다. 핵심은 cumsum 에 있다.

> pad_masks = 1D
>
> att_masks = 1D 
{: .prompt-info }

이 두친구들을 가지고 이제 2d 로 조합하는게 이 코드의 목적이다.

<div class="notion-gap" style="--gap: 1"></div>

#### att_masks 1D의 의미: 블록 경계 표시

처음에 이게 제일 헷갈렸는데, `att_masks`는 "보인다/안 보인다"가 아니라 **블록 경계**를 적어둔 것이다.

- **0** = 앞 토큰이랑 같은 블록 (cumsum 그대로)
- **1** = 여기서 새 블록 시작 (cumsum +1) → 앞 토큰들은 나를 못 본다

그리고 규칙은 딱 한 줄이다.

$$
\text{att\_2d}[i, j] = \text{cumsum}[j] \le \text{cumsum}[i]
$$

> 말로 하면 "**나보다 뒤 블록은 못 본다**"

pad는 att랑 상관없이 `pad[i] * pad[j]` 로 행, 열 둘 다 0이 된다.

<div class="notion-gap" style="--gap: 1"></div>

#### 손으로 한번 풀어보자

image 4개를 한 블록, state 3개를 causal로 두고 싶다면,

```python
tokens = [img1, img2, img3, img4, s1, s2, s3]
att    = [0,    0,    0,    0,    1,  1,  1]
cumsum = [0,    0,    0,    0,    1,  2,  3]

# att_2d[i, j] = cumsum[j] <= cumsum[i]
[1, 1, 1, 1, 0, 0, 0]
[1, 1, 1, 1, 0, 0, 0]
[1, 1, 1, 1, 0, 0, 0]
[1, 1, 1, 1, 0, 0, 0]   # image 1~4: 서로 full attention
[1, 1, 1, 1, 1, 0, 0]   # s1
[1, 1, 1, 1, 1, 1, 0]   # s2
[1, 1, 1, 1, 1, 1, 1]   # s3  -> state 끼리는 causal
```

실제로 메서드를 호출해보니 한 칸도 안 틀리고 똑같이 나왔다.

<div class="notion-gap" style="--gap: 1"></div>

#### 실습 코드

직접 `make_att_2d_masks`를 호출해서 4가지 패턴을 그려보자. (`phase1_smolvla/03_mask_practice.py`)

```python
from pathlib import Path
import torch
import matplotlib.pyplot as plt
from lerobot.policies.smolvla.modeling_smolvla import make_att_2d_masks

# (tokens, pad_masks, att_masks)
cases = {
    "my example":       (["img1","img2","img3","img4","s1","s2","s3"], [1,1,1,1,1,1,1], [0,0,0,0,1,1,1]),
    "smolvla prefix":   (["img1","img2","lang1","lang2","pad","state"], [1,1,1,1,0,1],  [0,0,0,0,0,1]),
    "full (all zeros)": (["t1","t2","t3","t4","pad"],                  [1,1,1,1,0],    [0,0,0,0,0]),
    "smolvla suffix":   (["a1","a2","a3","a4","a5"],                    [1,1,1,1,1],    [1,1,1,1,1]),
}
```

![](images/img-003.png)

> - `[0,0,0,0]` → full (BERT처럼 양방향)<br>- `[1,1,1,1]` → causal (GPT)<br>- `[0,0,1,1]` → prefix-LM: 앞 블록은 full, 뒤는 causal<br>- 맨 앞 값은 0이든 1이든 결과가 같다 (앞에 아무도 없으니까)<br>→ 결국 1D 리스트 하나로 블록 구조 전체를 표현하는 것이다.
{: .prompt-info }

<div class="notion-gap" style="--gap: 1"></div>

## 사용 코드

---

그럼 만든 mask는 어디서 쓰일까? 결국 **softmax 직전**에 쓰인다.

#### 1) Attention 안에서: 못 보는 칸을 -∞로

```python
# lerobot -> policies -> smolvla -> smolvlm_with_expert.py  (eager_attention_forward)

att_weights = torch.matmul(query_states, key_states.transpose(2, 3))   # [B, H, L_q, L_k]
att_weights *= head_dim**-0.5

big_neg = torch.finfo(att_weights.dtype).min                           # 사실상 -inf
masked_att_weights = torch.where(attention_mask[:, None, :, :], att_weights, big_neg)
probs = nn.functional.softmax(masked_att_weights, dim=-1)              # 0인 칸 -> 확률 0
```

- mask가 1인 칸은 점수 그대로, 0인 칸은 엄청 큰 음수로 바꿔버린다.
- softmax에서 $e^{-\infty} = 0$ 이니까 그 토큰은 **확률 0 = 아예 안 본 것**이 된다.
- `[:, None, :, :]` 는 head 축을 추가해서 15개 head 전부에 같은 mask를 쓰려는 것.
- 그럼 왜 진짜 -inf가 아니라 `finfo.min`(엄청 큰 음수)을 쓸까? padding 행처럼 한 줄 전체가 0인 경우가 있기 때문이다. 전부 -inf면 softmax가 0/0 = **NaN**이 되어버린다. 엄청 큰 음수를 쓰면 이런 행도 NaN 없이 그냥 균등분포로 끝난다. (어차피 padding 행의 결과는 안 쓴다)

<div class="notion-gap" style="--gap: 1"></div>

#### 2) SmolVLA에서 쓰이는 곳 2군데

**(a) Prefix prefill (KV cache 만들 때)**: 정사각형 `[B, L_p, L_p]` = `[1, 241, 241]`

```python
prefix_embs, prefix_pad_masks, prefix_att_masks = model.embed_prefix(images, img_masks, lang_tokens, lang_masks, state=state)
prefix_att_2d_masks = make_att_2d_masks(prefix_pad_masks, prefix_att_masks)    # [1, 241, 241]
```

**(b) Denoise step**: 직사각형 `[B, L_s, L_p + L_s]` = `[1, 50, 291]`

```python
# action(query 50개) -> prefix(cache 241개): 진짜 토큰이면 전부 봄
prefix_pad_2d_masks = prefix_pad_masks[:, None, :].expand(batch_size, suffix_len, prefix_len)   # [1, 50, 241]
# action -> action: causal
suffix_att_2d_masks = make_att_2d_masks(suffix_pad_masks, suffix_att_masks)                      # [1, 50, 50]
# key 축(dim=2)으로 이어붙이기
full_att_2d_masks = torch.cat([prefix_pad_2d_masks, suffix_att_2d_masks], dim=2)               # [1, 50, 291]
```

![](images/img-004.png)

- 빨간 선 왼쪽: KV cache(prefix 241), 오른쪽: 새로 들어온 action 50
- denoise 때는 action만 query로 들어오니까 정사각형이 아니라 **50 x 291 직사각형**이 된다.

> 정리하면, 1D 두 개(pad, att)로 블록 규칙을 적고 → `make_att_2d_masks`로 \[L, L\] 표를 만들고 → softmax 직전에 0인 칸을 -∞로 지워버린다. 이 세 단계가 mask의 전부다.
{: .prompt-info }

---
layout: post
title: "AI 시대 Game making and playing"
date: 2026-10-29 15:00:00 +0900
categories: [Study, AI]
section: Study
study_area: AI
topic: "Game"
tags: [game-design, flow, sdt, mda, claude-code, vibe-coding, ugc, world-model, ai-game-industry]
description: "사람은 왜 게임에 몰입할까? Flow, SDT, MDA로 재미의 원리를 정리하고, 바운스볼·Minecraft·LoL·Overcooked 사례에 적용해 본다. 그리고 혼자 Claude랑 게임을 만든다면 뭘 어떻게 만들지, AI 시대에 게임을 만드는 방식·플레이어·기업이 어떻게 바뀌고 있는지까지 살펴본다."
permalink: /blog/ai/game/ai-era-game-making-and-playing/
media_subpath: /blog/ai/game/ai-era-game-making-and-playing/
math: true
---

## Introduction

---

어쩌다 보니 게임을 제작을 하게 되었다. 하지만 재미있다. 새로운 것을 시도하고 배우는 것은 항상 재미있다. 진심이다. 자 여기서, 그러면 제작하기전에 원리를 이해하자. 인간은 왜 게임을 하며, 그 이유를 바탕으로 어떻게 게임을 만들어야 하며, 공식이 존재할까? 사례들을 보면서 살펴보자. 또한 AI 시대에 게임을 제작하는 방식, 기획하는 방식 사업의 방향성도(대기업)들도 많이 바뀌었을 것 같다. 그것 또한 한번 살펴보자 (시장의 변화)

## Contents

---

1. Psychology of Play: 인간은 `왜` 게임에서 즐거움을 느끼는가?
2. Game Design Theory: `어떻게` 설계해야 재미있는 게임이 되는가?
3. 실제 게임 유저를 많이 모은 사례
4. 재미의 공식은 만들 수 있을까?
5. 그래서 나 혼자 Claude랑 게임을 만든다면 `뭘`, `어떻게` 만들어야 할까?
6. 요즘 AI 시대에 사람들은 게임을 어떻게 만들고 있나?
7. 요즘 AI 시대 제작하는 게임의 변화. (소비자들자체가 변하고 있을테니)
8. 요즘 AI 시대 기업들의 사업 방향성 변화.

<div class="notion-gap" style="--gap: 1"></div>

## 1. 왜? — Psychology of Play

---

### 1a. Flow theory

---

![](images/img-001.png)

게임이 재미있어지는 데 보편적인 단일 공식은 없지만, 재미와 몰입을 설명하는 심리학적 이론과 설계 프레임워크는 존재한다. 아래는 그중 실제 게임 제작에 활용할 만한 핵심 개념을 정리한 내용이다.

#### Flow: 도전과 실력의 균형

**핵심 질문: 사람은 언제 몰입하는가?**

칙센트미하이(Csikszentmihalyi)의 Flow 이론에서는 **도전 수준과 개인의 능력 수준이 함께 높아지면서 균형**을 이룰 때 몰입이 일어나기 쉽다고 설명한다. 하지만 난이도 균형만으로 충분한 것은 아니고, 명확한 목표와 즉각적인 피드백 역시 중요하다.

> - 게임 난이도와 실력이 **반드시 linear하게 증가해야 한다는 의미는 아니다.** 플레이어에 맞는 도전 수준을 유지하는 것이 핵심이다.
> - 실력에 비해 지나치게 쉬우면 지루하다.
> - 실력에 비해 지나치게 어려우면 불안하거나 좌절한다.
> - 적절한 도전, 목표, 피드백이 결합하면 집중과 몰입이 촉진될 수 있다.
{: .prompt-tip }

<div class="notion-gap" style="--gap: 2"></div>

### 1b. Self-Determination Theory (SDT): 왜 자발적으로 계속 플레이할까?

---

Deci와 Ryan의 `자기결정성이론은` 인간의 동기를 설명하는 세 가지 기본 심리적 욕구에 주목한다.

| 욕구 | 의미 | 게임 디자인 예시 |
|---|---|---|
| **Autonomy (자율성)** | 스스로 선택한다는 느낌 | 목표를 달성하는 여러 경로 허용 |
| **Competence (유능감)** | 점점 능숙해진다는 느낌 | 적절한 난이도, 숙련도 피드백 |
| **Relatedness (관계성)** | 타인과 연결되어 있다는 느낌 | 협동, 공동 목표, 커뮤니티 |

`돈이나 포인트 같은 외적 보상만으로 장기적인 재미를 설명하기는 어렵다.` 플레이어가 스스로 선택하고 성장하며 타인과 연결된다고 느끼는 경험도 중요하다. (자율성과 유능감은 서로 연결될 수 있지만 반드시 순서대로 나타나는 것은 아니다. 승리나 외적 보상 없이도 성장의 경험 자체에서 유능감을 느낄 수 있다.)

<div class="notion-gap" style="--gap: 3"></div>

## 2. 어떻게? — MDA Framework: 재미를 어떻게 설계할까?

---

MDA는 Hunicke, LeBlanc, Zubek이 제시한 게임 디자인 프레임워크로, **Mechanics → Dynamics → Aesthetics**의 세 층위를 구분한다.

![](images/img-002.png)
_MDA 프레임워크: 디자이너가 설계한 규칙이 플레이 중 행동을 거쳐 플레이어의 경험을 형성한다. 출처: ESS Lab 게임 디자인 강의 자료_

| 층위 | 무엇을 뜻하나? | 예시 (슈퍼 마리오) |
|---|---|---|
| **Mechanics** | 규칙, 물리, 조작, 보상 시스템 | 달리기·점프, 적 밟기, 코인·버섯, 제한 시간 |
| **Dynamics** | 플레이 중 실제로 나타나는 상호작용 | 타이밍 맞춰 점프, 숨은 길 찾기, 실패 후 재도전 |
| **Aesthetics** | 플레이어가 경험하는 감정과 재미 | 도전, 발견, 성취감 |

재미 자체를 코딩하기보다 **`재미를 유발할 수 있는 규칙을 설계`한다**고 이해하면 된다. 또한 디자이너는 `원하는 경험`에서 출발해 역방향으로 규칙을 설계할 수 있다.

**Dynamics는 기계공학적 운동만 뜻하지 않는다.** 규칙 아래에서 발생하는 플레이어의 전략, 협동, 반복 시도, 상호작용 등도 포함한다.

MDA의 Aesthetics는 시각적인 그래픽만 의미하지 않는다. `감각적 즐거움, 판타지, 서사, 도전, 관계, 발견, 표현, 몰입` 등 넓은 플레이 경험을 말한다.

원문: [MDA: A Formal Approach to Game Design and Game Research (2004)](https://www.cs.northwestern.edu/~hunicke/MDA.pdf)

<div class="notion-gap" style="--gap: 3"></div>

## 3. 실제 게임 사례: 세 이론을 함께 적용해 보기

재미를 설계하는 관점에서 **Flow와 SDT는 사람의 심리적 동기를 설명하고, MDA는 게임의 규칙·행동·경험을 구조적으로 분석하는 도구**다. 아래 해석은 각 게임 개발사가 세 이론을 의도적으로 사용했다는 주장이 아니라, 이론에 비추어 게임을 분석한 것이다.

### 3a. 바운스볼 (Bouncy Ball) — 스테이지와 숙련의 성장

![](images/img-003.png)

- **Flow:** 좌우 이동이라는 단순한 조작을 학습한 뒤, 새로운 장애물과 퍼즐 요소가 등장하면서 단계적으로 도전이 늘어난다. 실력과 난이도가 반드시 직선으로 증가하는 것은 아니다. 잠깐 쉬운 구간이나 도전적인 구간이 있어도 전체적으로 적절한 균형을 유지하는 것이 중요하다.
- **SDT:** 어느 경로로 별을 얻을지 직접 판단하는 자율성, 시행착오 끝에 스테이지를 해결하는 유능감이 핵심이다. 관계성은 이 게임의 필수 요소는 아니다.
- **MDA:** Mechanics = 좌우 조작·점프/충돌·별 수집·장애물 / Dynamics = 경로 탐색·타이밍 조절·실패 후 재시도 / Aesthetics = 도전·발견·성취감.

**시사점:** 조작은 간단하게 만들고, 상황과 제약을 바꾸면서 유저가 새로운 해결 방법을 찾게 한다.

참고: [바운스볼 Google Play 공식 소개](https://play.google.com/store/apps/details?id=com.raongames.bouneball)

### 3b. Minecraft — 외적 보상 없이도 재미있는 이유

![](images/img-004.jpg)
_Minecraft 실제 플레이 화면. 출처: Instant Gaming_

- **Flow:** 스스로 쉬운 건축부터 복잡한 구조물이나 생존 과제로 목표를 설정할 수 있다. 따라서 정해진 스테이지 난이도가 없어도 몰입이 가능하다.
- **SDT:** 무엇을 만들지 결정(자율성), 더 복잡한 건축·자동화에 성공(유능감), 친구와 공동 세계를 구축(관계성). 보상이나 승리가 없어도 놀이가 지속될 수 있음을 잘 보여준다.
- **MDA:** Mechanics = 블록 배치·채굴·제작·월드 규칙 / Dynamics = 창작·탐험·자원 계획·협업 / Aesthetics = 표현·발견·판타지·성취감.

**시사점:** 플레이어가 **자기 목표를 만드는 것 자체**가 강력한 참여 동기가 될 수 있다.

### 3c. League of Legends — 개인 숙련과 팀 관계

![](images/img-005.jpg)
_League of Legends 팀 교전 화면. 출처: Famitsu_

- **Flow:** 챔피언 숙련도·전략 이해·상대의 강함에 따라 매 경기 새로운 도전이 발생한다. 실제 매칭이 항상 적절한 난이도를 보장하지는 않는다.
- **SDT:** 챔피언과 빌드·동선을 선택(자율성), 숙련·실력 향상(유능감), 팀 협동과 소속감(관계성). 반드시 승리해야만 유능감을 느끼는 것은 아니다.
- **MDA:** Mechanics = 챔피언 스킬·자원·오브젝트·팀 규칙 / Dynamics = 라인전·교전·역할 분담·심리전 / Aesthetics = 경쟁·긴장·협력·승리의 성취감.

**시사점:** 협동은 단순히 플레이어를 한 공간에 모아 놓는 게 아니라, **서로 의존하는 목표와 역할**을 줄 때 더 강하게 발생한다.

### 3d. Overcooked! 2 — MDA가 가장 선명하게 보이는 사례

![](images/img-006.jpg)
_Overcooked! 2 공식 게임플레이 화면. 출처: Team17_

- **Flow:** 단순한 조리 작업에서 시작해 다양한 레시피, 분리된 조리대, 이동 경로와 시간 압박 등이 추가된다.
- **SDT:** 누가 어떤 역할을 수행할지 결정(자율성), 더 빠르고 효율적으로 주문 처리(유능감), 동료와 함께 위기를 극복(관계성).
- **MDA Mechanics:** 재료를 집고, 자르고, 요리하고, 서빙한다. 주문과 제한 시간이 있다.
- **MDA Dynamics:** 플레이어들이 역할을 나누고, 재료를 전달하고, 동선이 꼬이면 즉흥적으로 협력한다.
- **MDA Aesthetics:** 긴박감·혼란·웃음·협동의 성취감.

여기서 **개발자가 직접 설계한 것은 재료를 자르는 규칙이지만, 플레이어가 경험하는 재미는 역할 분담과 혼란을 극복하는 과정에서 발생할 수 있다**는 점이 중요하다.

참고: [Team17 공식 Overcooked! 2 소개](https://www.team17.com/news/introducing-overcooked-2)

### 사례 비교 요약

| 게임 | 특히 두드러지는 경험 | 설계할 때 가져갈 포인트 |
|---|---|---|
| 바운스볼 | 적절한 도전과 문제 해결 | 조작은 단순하게, 상황·제약으로 난이도 올리기 |
| Minecraft | 자율적 창작과 발견 | 플레이어가 목표·경로를 직접 고르게 하기 |
| League of Legends | 숙련과 팀 협동 | 역할 분담·공동 목표·반복 숙련 |
| Overcooked! 2 | 시간 압박 속 협력과 혼란 | 시간 압박 + 서로 의존하는 역할 분담 |

<div class="notion-gap" style="--gap: 2"></div>

## 4. 재미의 공식은 만들 수 있을까?

---

모든 플레이어에게 동일하게 적용되는 과학적으로 확립된 단일 재미 공식은 없다. 다만 가설을 검증하기 위한 **개념적 모델**은 구성할 수 있다.

$$
F = w_1 C + w_2 A + w_3 R + w_4 L - w_5 X
$$

여기서 $C$는 유능감, $A$는 자율성, $R$은 관계성, $L$은 도전과 몰입, $X$는 좌절과 불편이다. 이 식은 검증된 심리학 법칙이 아니라 **실험용 가설식**이다. 사람마다 선호도가 다르고 요소 사이에 비선형 상호작용이 존재할 수 있다.

실제로는 플레이 시간 하나보다 자발적 재참여율, 난이도별 이탈률, 반복 플레이 횟수, 주관적 재미 평가를 함께 봐야 한다.

<div class="notion-gap" style="--gap: 3"></div>

## 5. 그래서 나 혼자 Claude랑 게임을 만든다면?

---

여기까지 이론을 봤는데, 사실 진짜 궁금한 건 이거다. **"나 혼자 Claude랑 게임을 만든다면, 뭘 어떻게 만들어야 할까?"**

결론부터 말하면, 2026년 지금 코드를 짜는 비용은 거의 0에 가까워졌다. Claude한테 "이런 게임 만들어줘" 하면 몇 분 만에 플레이 가능한 버전이 나온다. 그런데 **"이게 재미있나?"는 Claude가 대신 판단해 주지 못한다.** 결국 1인 + AI 개발에서 병목은 코딩이 아니라 `무엇을 만들지 고르는 것`과 `직접 플레이해 보고 고치는 루프`다.

<div class="notion-gap" style="--gap: 1"></div>

### 5a. 뭘 만들까: 작게, 그리고 재미 하나만 선명하게

첫 게임에서 제일 흔한 실패는 기술이 아니라 scope다. "오픈월드 RPG + 멀티플레이" 이런 거 잡으면 Claude가 있어도 거의 무조건 망한다. 아래 기준으로 고르면 된다.

| 기준 | 왜? |
|---|---|
| core loop를 한 문장으로 설명 가능 | 한 문장이 안 나오면 Mechanics가 너무 많다는 뜻 |
| 한 판이 1~5분 | 플레이테스트를 하루에 수십 번 돌릴 수 있다 |
| 콘텐츠를 손으로 많이 안 만들어도 됨 | 규칙 조합·절차적 생성으로 다양성을 만든다 (스테이지 수백 개를 손으로 ✕) |
| 브라우저에서 바로 실행 | 링크 하나로 친구한테 바로 플레이시킬 수 있다 |
| 아트가 단순해도 성립 | 사각형으로도 재미있어야 진짜 재미있는 거다 |

→ 이 기준이면 **퍼즐, 아케이드, 로그라이트, 짧은 물리 게임**이 잘 맞는다. 반대로 서사 중심 RPG, 온라인 멀티플레이, 대규모 오픈월드는 첫 작품으로는 피하는 게 좋다. (스토리 퀘스트는 버그 하나가 진행을 통째로 막아버리고, 네트워크 동기화는 AI한테 맡겨도 디버깅 지옥이다.)

앞에서 본 이론을 체크리스트로 바꾸면 이렇게 된다.

1. **MDA를 거꾸로:** 원하는 Aesthetics 하나를 먼저 정한다. e.g) "아슬아슬하게 성공하는 쾌감", "같이 허둥대다가 웃기는 협동"
2. 그 경험을 만들 **Mechanics를 3개 이하**로 고른다.
3. **Flow:** 첫 30초 안에 조작을 배우게 하고, 난이도는 스테이지·규칙을 바꾸는 방식으로 올린다 (바운스볼 방식).
4. **SDT:** 정답 경로를 하나로 막지 말고 여러 방법으로 풀 수 있게 열어둔다 (자율성). 관계성(멀티)은 2탄에서.

<div class="notion-gap" style="--gap: 1"></div>

### 5b. 어떻게 만들까: Claude와의 개발 루프

![](images/img-007.png)

**0) 엔진 고르기**

| 선택지 | 장점 | 단점 | 추천 |
|---|---|---|---|
| 웹 (Phaser = 2D, three.js = 3D) | Claude가 제일 잘 다룸, 링크로 바로 공유, 빌드 과정 없음 | 큰 3D 게임엔 한계 | **첫 작품은 이거** |
| Godot | 무료·가벼움, MCP 서버를 붙이면 Claude가 씬/노드를 직접 조작하고 실행 에러까지 읽음 | 에디터 학습 필요 | 본격적으로 2D/3D 갈 때 |
| Unity / Unreal | 생태계·에셋 최강 | 무겁고, 에디터 작업이 많아서 에이전트가 손대기 어려운 부분이 많음 | 팀 단위 / 상용 목표일 때 |

**1) Spec 1장 먼저 쓰기** — Claude에게 넘길 기획서다. Claude Code라면 이걸 `GAME_SPEC.md`나 `CLAUDE.md`로 두면 매번 다시 설명 안 해도 된다.

```markdown
# GAME_SPEC.md
- 목표 경험(Aesthetics): 아슬아슬하게 성공하는 쾌감
- Core loop (1문장): 물체를 집어 → 장애물을 피해 → 목표 칸에 놓는다
- 조작: 마우스 드래그만
- Mechanics (3개 이하): 집기/놓기, 물리 충돌, 제한 시간
- 승리/실패: 시간 안에 모든 물체 배치 / 시간 초과·물체 낙하
- 난이도 곡선: 1~3스테이지 튜토리얼 → 물체 수 → 장애물 → 시간 제약 순으로 증가
- 기술: Phaser 3, 단일 HTML, 모바일 대응
- 하지 말 것: 아트·사운드는 나중에, 멀티플레이 X
- 튜닝값(속도, 중력, 제한 시간)은 전부 config.js 한 곳에 모을 것
```

**2) Graybox 프로토타입** — 아트 없이 사각형·원만으로 1~2시간 안에 플레이 가능한 버전을 만든다. 이때 질문은 딱 하나다. `사각형으로도 재미있나?`

**3) 내가 직접 플레이 → 느낌을 말로 피드백** — 여기가 사람의 일이다. "점프가 너무 무겁다", "3스테이지부터 갑자기 어렵다", "죽고 다시 시작하는 데 3초나 걸린다" 같은 피드백을 준다. game feel(조작감)은 AI가 손으로 느끼질 못하기 때문에, **수치를 config나 화면 위 튜닝 패널(슬라이더)로 빼달라고 해서 내가 직접 만지는 게** 훨씬 빠르다.

**4) 자동 검증은 Claude에게** — Claude Code는 브라우저를 띄워서 스크린샷을 찍고 콘솔 에러를 읽을 수 있다. 여기에 봇 플레이(랜덤/탐색 에이전트)로 "모든 스테이지가 클리어 가능한가", "소프트락은 없나"를 체크하게 하면, 나는 재미에만 집중할 수 있다.

**5) 남에게 시켜보기** — 설명 없이 친구 3~5명한테 링크만 주고 지켜본다. 어디서 막히고 어디서 그만두는지가 제일 정직한 데이터다. 4장에서 말한 재시도 횟수·스테이지별 이탈률 같은 로그를 이때부터 남겨두면 좋다.

**6) 재미가 확인된 후에 Polish** — 그제서야 아트, 3D 모델(Meshy 같은 image→3D 도구), 사운드, 이펙트(juice: 화면 흔들림, 파티클, 타격음)를 붙인다. 순서가 바뀌면 재미없는 게임을 예쁘게 만드는 데 시간을 다 쓰게 된다.

> **나만의 언어:** Claude = 손이 엄청 빠른 개발자, 나 = 디렉터 겸 첫 번째 플레이어. 손은 빌려도 되지만 "재미있다"는 판단은 위임이 안 된다.
{: .prompt-info }

<div class="notion-gap" style="--gap: 3"></div>

## 6. 요즘 AI 시대에 사람들은 게임을 어떻게 만들고 있나

---

![](images/img-008.png)

### 업계 분위기: 쓰는 사람은 늘었는데, 분위기는 차갑다

GDC 2026 State of the Game Industry 설문(2,300명+)을 보면 응답자의 약 36%가 업무에 생성형 AI를 쓰고 있다. 그런데 **"생성형 AI가 업계에 해롭다"는 응답이 52%**로, 1년 전 30%, 2년 전 18%에서 계속 올라갔다. 특히 아트, 게임 디자인·내러티브, 프로그래머 직군에서 부정적인 비율이 높다.

→ 그래서 AI로 만든 아트·음성이 들어간 게임은 유저 반감을 살 수 있다는 걸 알고 가야 한다. Steam도 AI 생성 콘텐츠를 쓰면 스토어 페이지에 공개하도록 하고 있다.

### 패턴 ①: Vibe coding으로 웹 게임 통째로 만들기

Simon Willison이 바로 어제(2026-10-28) 쓴 글이 딱 이 이야기다. Claude Opus 5.5로 게임 4개를 만들었는데, 전부 브라우저에서 도는 HTML/JS 게임이고 코드는 직접 읽지 않았다고 한다.

- 숨은그림찾기류 게임(Tree Appreciator)은 프롬프트 한 번에 완성
- RTS 게임(Battle Drones)은 첫 버전이 재미없었는데, "Make it a LOT more fun" 한 마디로 훨씬 재미있어졌다고 함
- 규모가 커지면 spec 파일로 기획을 먼저 쓰고 Claude Code로 이어서 개발
- 반대로 농장 시뮬레이션은 이틀 가까이 돌렸는데도 메커니즘이 너무 복잡해서 아직 설득력이 없다고 함 → 범위가 크면 AI도 재미를 못 잡는다. 5a에서 말한 "작게"가 괜히 나온 말이 아니다.

### 패턴 ②: 엔진 에디터에 에이전트 붙이기 (MCP)

Godot, Unity 같은 엔진에 MCP 서버를 붙여서, Claude Code가 씬·노드·스크립트를 직접 만들고 게임을 실행해서 실제 에러 로그를 읽고 다시 고치게 하는 방식이다. (Godot은 오픈소스 godot-mcp가 많이 쓰인다.) 핵심은 `게임을 직접 실행해 볼 수 있는 에이전트`가 코드만 보고 고치는 에이전트보다 훨씬 잘 만든다는 것.

### 패턴 ③: 에셋 생성 파이프라인

컨셉 이미지 생성 → image→3D → 자동 리깅 → 애니메이션까지 AI 도구로 이어서 뽑는다. 1인 개발자의 제일 큰 구멍인 아트를 메워주지만, 위에서 본 것처럼 반감도 제일 큰 영역이다.

### 패턴 ④: 에이전트가 플레이어·테스터

봇이 레벨을 돌려 클리어 가능성과 버그를 체크하고, 아예 LLM끼리 대전시키는 모드를 넣기도 한다 (Battle Drones에도 LLM vs LLM 모드가 있다). 게임 안의 NPC 대사·행동을 LLM이 실시간으로 만드는 시도도 늘고 있다.

### 그래서 정리하면

인디 개발자들이 공통적으로 하는 말은 비슷하다. 에이전트는 scaffolding, 보일러플레이트, 테스트, 에셋 파이프라인 스크립트, 반복 수정은 잘하지만 **game feel 튜닝, 세이브 시스템, 성능 디버깅, 그리고 "뭐가 재미있는지"**는 아직 사람 몫이다. 큰 코드베이스에서 에이전트를 완전히 풀어두면 몇 시간 일하고 못 쓰는 결과를 내놓기도 해서, 사람이 감독하는 중간 단계가 현실적이다.

!!코드 짜는 비용이 0에 가까워질수록, 오히려 앞에서 본 Flow·SDT·MDA 같은 "재미를 보는 눈"이 더 중요해진다!! 결국 AI 시대 게임 개발의 경쟁력은 구현력이 아니라 `취향`과 `플레이테스트 루프`다.

<div class="notion-gap" style="--gap: 3"></div>

## 7. 요즘 AI 시대 제작하는 게임의 변화: 플레이어 자체가 바뀌고 있다

---

![](images/img-009.png)

먼저 짚고 갈 것. 1~2장에서 본 **재미의 원리(Flow, SDT)는 AI 시대라고 안 바뀐다.** 사람이 몰입하고, 계속 하고 싶어지는 이유는 그대로다. 바뀐 건 `누가 만드는지`, `얼마나 많이 만들어지는지`, `어떻게 퍼지는지`, 그리고 `플레이어가 AI를 보는 눈`이다.

### 7a. 플레이어가 곧 제작자 (prompt-to-game)

2026년에 제일 큰 변화는 이거다. 플레이어가 프롬프트 몇 줄로 게임을 만들어서 바로 올린다.

- **Roblox Build**(2026년 7월), **Meta Horizon Create**, **Google Playground**, 그리고 Astrocade, Sekai 같은 스타트업까지 → Naavik이 테스트한 플랫폼 전부 20분 안에 플레이 가능한 게임이 나왔다고 한다.
- Roblox Build 뉴질랜드 알파에서 게임을 만든 사람의 **71%가 Roblox Studio를 한 번도 안 써본 사람**이었다. 즉, 원래 개발자가 아니던 사람들이 제작자로 들어오고 있다.
- 대부분 폰에서 만들 수 있어서, 모바일 위주 시장까지 UGC가 열렸다.

### 7b. 게임이 "작품"에서 "콘텐츠"로

예전에는 게임 = 한 번 사서 오래 하는 작품이었다면, 이제는 피드에서 넘기면서 해보는 숏폼에 가까워지고 있다. Sekai에서는 미니앱이 1,500만 개 만들어졌고, Fortnite에는 활성 게임이 32만 5천 개가 넘는다.

근데 여기서 재미있는 데이터가 있다.

- Sensor Tower 기준, Astrocade·Sekai 설치자 중 **30일 후에도 남아있는 비율은 약 3%**. Roblox는 약 17%.
- Roblox 상위 1,000개 경험이 전체 플레이 시간의 약 80%를 차지한다.
- Roblox 예시 중에는 플레이테스트 점수 100/100인데 **재플레이(replayability) 점수는 0**인 Build 게임도 있었다.

→ !!만드는 건 누구나 하게 됐는데, 계속 하게 만드는 건 여전히 어렵다!! 공급이 폭발하니까 오히려 1b에서 본 SDT(유능감·관계성)를 제대로 설계한 게임만 살아남는 구조다. "더 많이 만들어진다 ≠ 더 많이 플레이된다".

### 7c. 유통: 스토어보다 크리에이터·친구

BCG 2026 게임 리포트에 따르면, 설문한 게이머의 **55%가 "좋아하는 크리에이터가 새 게임으로 옮기면 따라가서 해볼 것"**이라고 답했다. 2024년 Roblox와 Fortnite가 크리에이터에게 지급한 돈만 각각 9.23억 달러, 3.52억 달러다. 게임이 퍼지는 경로가 스토어·광고에서 크리에이터·친구 공유로 옮겨가고 있다.

### 7d. AI를 보는 플레이어의 눈: "도구는 OK, 보이는 지름길은 NO"

AI로 만든 게임은 확 늘었다. PC Gamer 집계로 Steam 신작 중 AI 사용을 공개한 비율이 2024년 10.9% → 2025년 19.9% → 2026년(7월 기준) 30.8%. 2026년 10월 Next Fest에서는 7,240개 중 2,502개(34.6%)가 AI 사용을 공개했다. 그런데 **인기 상위 25개 데모 중에는 단 2개**뿐이었다.

플레이어 반응도 꽤 확실하다.

- **Arc Raiders**: AI TTS 음성으로 출시했다가 반발을 사서, 일부 대사를 실제 성우로 다시 녹음. (게임 자체는 판매·평가 모두 잘 나왔다.)
- **Clair Obscur: Expedition 33**: 플레이스홀더로 쓴 AI 텍스처가 출시 버전에 남아있던 게 알려지면서 Indie Game Awards의 GOTY가 취소됨(2025-12).
- Battlefield 6 유료 스티커 팩도 "AI로 만든 것 같다"는 이유로 반발.

→ 플레이어는 개발 도구로 AI 쓰는 것 자체보다, **돈 내고 보는 결과물에서 AI 티가 나는 것**에 반응한다. 1인 개발자 입장에서는 코드·테스트·플레이스홀더는 AI로 마음껏 쓰고, 최종적으로 눈과 귀에 닿는 부분은 신경 써야 한다는 뜻이다.

### 7e. 아예 새로운 종류의 게임: AI-native

LLM이 NPC 대사와 행동을 실시간으로 만드는 게임, 그리고 Google Genie 같은 world model이 프롬프트로 걸어다닐 수 있는 세계를 바로 생성하는 것까지 나오고 있다. 다만 world model은 아직 720p, 수십 fps, 장면 기억이 1분 남짓이라 "게임"이라기보다 데모에 가깝다.

<div class="notion-gap" style="--gap: 3"></div>

## 8. 요즘 AI 시대 기업들의 사업 방향성 변화

---

![](images/img-010.png)

기업들은 크게 4가지 방향으로 움직이고 있다. 한 줄로 말하면 **"파이프라인에는 AI를 깊게, 유저 눈에 보이는 곳에는 조심스럽게"**다.

### 8a. 대형 퍼블리셔: AI-First 전환 (= 비용 효율)

- **Krafton**: "AI First" 회사로 전환을 선언. 업무 자동화용 agentic AI와 게임 안 AI 서비스를 두 축으로, 약 1,000억 원 규모 GPU 클러스터를 투자했고 2026년 하반기까지 AI 플랫폼·데이터 기반을 완성하는 게 목표.
- **EA**: Stability AI와 생성형 AI 모델·툴·워크플로를 같이 개발. EA를 비상장으로 사들인 투자자들은 AI로 비용을 줄여 이익을 높이는 쪽에 베팅하고 있다는 분석이 많다.
- **Ubisoft**: La Forge 연구조직에서 Ghostwriter(NPC 잡담 대사 초안 생성) 같은 툴. "작가를 대체하는 게 아니라 반복 작업을 줄이는 것"이라는 입장.

→ 공통점은 `제작비·인력 효율`. 그리고 이게 GDC 2026 설문에서 개발자들의 반감이 커진 이유와 연결된다 (해고 + AI가 같이 이야기되니까).

### 8b. UGC 플랫폼: 툴을 소비자에게 주고, 생태계를 먹는다

Roblox, Meta, Google은 게임을 직접 만드는 대신 **누구나 게임을 만들 수 있는 툴**을 뿌린다. Roblox는 3D 생성 모델 Cube도 오픈소스로 풀고 Studio에 넣었다. 콘텐츠 공급은 유저가 하고, 플랫폼은 노출(알고리즘)과 결제·광고를 쥔다. 결국 7장에서 본 "플레이어가 곧 제작자"의 반대편에 이 사업 모델이 있다.

다만 Naavik 분석처럼 AI 프롬프트 툴 자체는 점점 흔해지고 있어서(commoditize), 승부는 툴이 아니라 **이미 플레이어가 모여 있는 플랫폼과 리텐션**에서 난다.

### 8c. 빅테크: World model 경쟁

- **Google DeepMind Genie**: Genie 3(2025-08) → 일반 공개 Project Genie(2026-01) → Genie 4(2026-10 보도). Genie가 나왔을 때 하루 만에 Unity 주가가 20% 넘게, Roblox·Take-Two도 두 자릿수로 빠졌다. 시장이 "게임 엔진이 필요 없어지는 것 아냐?"라고 반응한 것.
- **Microsoft Muse**(Nature, 2025-02): Ninja Theory와 만든 "World and Human Action Model". 사람이 실제로 플레이한 게임 데이터(화면 + 컨트롤러 입력)로 학습해서, 다음 화면과 다음 행동을 생성한다.

여기서 중요한 포인트는 빅테크가 world model을 **게임만 보고 만드는 게 아니라는 것**이다. Google은 world model을 AGI로 가는 핵심 재료로, 로봇·에이전트 학습 환경으로 본다.

### 8d. 반작용: "사람이 만든" 것이 브랜드가 된다

Clair Obscur의 Sandfall은 GOTY 취소 이후 "앞으로 전부 사람이 만든다"는 입장을 냈고, Arc Raiders의 Embark도 "진짜 성우가 AI보다 낫다"며 AI 음성을 줄이고 있다. AI를 안 쓴다는 것 자체가 마케팅 포인트가 되는 흐름이다.

### 그래서 정리하면

| 주체 | 방향 | 돈이 되는 지점 |
|---|---|---|
| 대형 퍼블리셔 | AI-First, 제작 파이프라인 자동화 | 제작비·인력 절감 |
| UGC 플랫폼 | 제작 툴을 소비자에게 | 플랫폼 수수료·광고, 크리에이터 생태계 |
| 빅테크 | World model | 게임 너머(AGI, 로봇, 에이전트 학습) |
| 일부 스튜디오 | No-GenAI 브랜딩 | 신뢰·팬덤 |

<div class="notion-gap" style="--gap: 3"></div>

## 9. 핵심 정리

---

- 몰입(Flow) = 도전과 실력의 균형 + 명확한 목표 + 즉각적인 피드백
- 계속 하게 만드는 힘(SDT) = 자율성·유능감·관계성. 외적 보상만으로는 오래 못 간다
- 재미는 직접 코딩하는 게 아니라, 재미가 나올 규칙(Mechanics)을 설계하는 것 (MDA)
- 재미의 단일 공식은 없다 → 가설식 + 지표로 검증한다
- 혼자 Claude랑 만든다면: 작게, core loop 한 문장, 웹 graybox부터
- Claude는 손, 나는 디렉터 겸 첫 번째 플레이어 → "재미있다"는 판단은 위임 불가
- AI 시대 개발: 쓰는 사람은 늘었지만 반감도 커졌다. 코드보다 취향과 플레이테스트가 경쟁력
- 플레이어 변화: 누구나 만들게 됐다 → 공급 폭발 → "계속 하게 만드는 것"이 더 희귀해졌다. AI는 도구로는 OK, 보이는 결과물에서는 반발
- 기업 변화: 퍼블리셔는 AI-First로 비용 효율, 플랫폼은 툴을 뿌려 생태계 장악, 빅테크는 world model → 사람의 플레이 데이터 가치가 올라간다

<div class="notion-gap" style="--gap: 1"></div>

### 참고 자료

- [Hunicke et al. (2004), MDA Framework](https://www.cs.northwestern.edu/~hunicke/MDA.pdf)
- [Self-Determination Theory 공식 사이트](https://selfdeterminationtheory.org/theory/)
- Csikszentmihalyi, M. (1990). Flow: The Psychology of Optimal Experience
- [GDC 2026 State of the Game Industry](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/)
- [Simon Willison — The October inflection point for vibe game development (2026-10-28)](https://simonwillison.net/2026/Oct/28/vibe-game-development/)
- [Coding-Solo/godot-mcp (GitHub)](https://github.com/Coding-Solo/godot-mcp)
- [Althera Games — AI Agents for Game Development 2026](https://altheragames.com/en/blog/ai-agents-game-development-2026)
- [Naavik — Prompt-to-Game Is Here. Which Platforms Are Positioned to Win? (2026-10)](https://naavik.co/ai-gaming/prompt-to-game-is-here-which-platforms-are-positioned-to-win/)
- [BCG — Video Gaming Report 2026](https://www.bcg.com/publications/2025/video-gaming-report-2026-next-era-of-growth)
- [PC Gamer — Steam AI disclosure 추이](https://www.pcgamer.com/gaming-industry/steam-week-in-review-take-cover-because-it-looks-like-more-than-half-of-steam-games-will-have-an-ai-disclosure-by-2027-2028/)
- [PCGamesN — Arc Raiders AI 음성 교체](https://www.pcgamesn.com/arc-raiders/ai-voices-replaced)
- [Stevivor — Clair Obscur, Indie Game Awards 수상 취소](https://stevivor.com/news/clair-obscur-loses-two-indie-game-awards-due-to-ai-usage/)
- [Game Developer — Krafton AI First](https://www.gamedeveloper.com/business/subnautica-owner-krafton-outlines-plans-to-transform-into-an-ai-first-company)
- [Decrypt — EA·Krafton 생성형 AI 전략](https://decrypt.co/345847/gaming-giants-electronic-arts-krafton-going-big-generative-ai)
- [Wikipedia — Genie (world model)](https://en.wikipedia.org/wiki/Genie_%28world_model%29)

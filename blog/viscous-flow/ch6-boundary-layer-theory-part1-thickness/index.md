---
title: "Ch6 Boundary Layer theory part1 - thickness"
layout: single
author_profile: false
sidebar:
  nav: "docs"
source_url: "https://jeffdissel.tistory.com/147"
source_id: "147"
date: "2024-12-12T13:45:15+09:00"
category: "Viscous-Flow"
---

Source: [https://jeffdissel.tistory.com/147](https://jeffdissel.tistory.com/147)

고체 surface위를 유체가 흐르는 경우,
no-slip boundary condition
(속도 = 0 on the surface)
+ 점성효과로 인하여,
고체 표면 근처에서 속도장은
Free stream Velocity (U∞)과 다르다.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-001.jpg)
그 속도가 감소한 영역을,
boundary layer이라고 하는 것은
익숙하여 다들 아실 것이다.
이제 수학적으로 boundary layer의
thickness, shear stress, pressure difference는 어떻게 되는지,
분석해보자.
다음과 같이, 비행기의 날개 주변에 생긴
boundary layer를 살펴보자.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-002.png)
boundary layer thickness 실험적으로 측정했을때,
사실 굉장히 작다.
따라서, 우리는 curvature를 무시하고
flat plate라고 생각을 한후,
Steady 2D Boundary flow
Equations들을 적용시킬 수 있다.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-003.png)
1. 연속방정식, 2,3 모멘텀 보존방정식(Navieres stokes eq, x,y방향)
여기서 ch5에서 했던 방식으로
order of magnitude
로
위 식에서 어느 항이 의미있는 값을 가지고 있고,
어느 항이 소거될 만큼 작은 (상대적인)크기를 가지고 있는지
확인해보자.
먼저 1번 연속방정식을 통해 y방향 속도의 크기는 다음과 같다.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-004.png)
2번 x방향 모멘텀 방정식을 order of magnitude로 분석을 해보면,
![Ch6 Boundary Layer theory part1 - thickness](./images/img-005.png)
boundary layer thickness가 굉장히 작으므로,
![Ch6 Boundary Layer theory part1 - thickness](./images/img-006.png)
우항 d^2u/dx^2을 소거할 수 있다.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-007.png)
같은 방식으로 3번식은 dp/dy 빼고 전부 소거된다.
#소거의 의미
order of magnitude 분석시, 굉장히 작은 값
= (상대적으로)무의미한 값
![Ch6 Boundary Layer theory part1 - thickness](./images/img-008.png)
여기서 재미있는 사실은 3'식을 통해서,
우리는 Boundary layer 안과 밖의 압력이 (같은x일때)
y에 따라 변화가 없음을 알 수 있다.
-> P_b = P_a
![Ch6 Boundary Layer theory part1 - thickness](./images/img-009.png)
boundary layer밖은 점성의 효과가 없는 영역이다
+ Irrotational incompressible 가정을 더해주면 = potential flow가 된다.
-
> State B에 대하여 Bernoulli Eq 적용가능.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-010.png)
이후 Pa = Pb를 이용하여,
여기서 아주 중요한 4번식이 유도된다.
이제 order of magniutde로 1,2,3식을 다듬으면,
다음과 같이 1,6식이 도출되고,
이를 Boundary layer Eq이라고 부른다.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-011.png)
가장 중요한 boundary condition은 다음과 같다.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-012.png)
____________________________
자 지금까지 boundray layer equation (1,6)을 유도하였다.
이 방정식을 꼭 계속해서 기억하고, 이를 이용하여
이제 우리가 진짜 풀고싶은 문제
boundary layer thickness 구하기,
shear stress구하기 등등을 풀어보자.
____________________________
[boundary layer thickness, δ ]
가장 큰 고민은 저 viscous region layer두께가 얼마일까?
x에 따라서 증가하는 것 같은데
어떻게 증가하는지 식을 세울 수 있나?
라는 질문을 프란들은 품었고 이를 수학적으로 풀었다.
이를 풀기전에 몇가지 개념을 정의하고 가야한다.
(차근차근 천천히 가보자.)
a) Momentum Thickness, θ
다음과 같이 flat plate boundary layer유체를 살펴보자.
빨간색 눕힌 사다리꼴
을
Control volume
이라고 정의하고
분석 할 것이다.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-013.png)
flat plate boundary layer w/ a stream line.
Reynolds transport theorem(유체역학 포스터)
을 활용하여,
들어오고 나가는 mass flux가 같아야 함을 이용하자.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-014.png)
위 식을 정리하면 7번 관계식이 나온다.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-015.png)
(추후에 쓰임, 곧 쓰임)
이번에는 Reynolds Transport theorem
-Momentum Conservation on Control Volume식
을 세워보자.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-016.png)
우리가 위에서 정의한 빨간색 눕혀진 사다리꼴 CV에 적용하자.
(알짜힘 = -x방향 Drag foce)
![Ch6 Boundary Layer theory part1 - thickness](./images/img-017.png)
쭉 전개하면 D를 정리할 수 있다.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-018.png)
여기서 빨간색 밑줄친 항에 아까 유도한 7번식을 대입해주자.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-019.png)
연속방정식 Reynolds transport theorem에서 유도.
정리하면, 최종적으로 8번식으로 drag force가
한개의 integral 로 정리된다.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-020.png)
![Ch6 Boundary Layer theory part1 - thickness](./images/img-021.png)
![Ch6 Boundary Layer theory part1 - thickness](./images/img-020.png)
![Ch6 Boundary Layer theory part1 - thickness](./images/img-021.png)
8번식을 보면, 우리가 u = u(y)식을 알면,
drag force를 boundary layer thickness에 관한
함수로 나타낼 수 있다.
(추후에 u(y) 식 가정하고 대입할 예정)
여기서 drag force는 사실 고체면과의 shear stress의 적분 값이다.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-022.png)
여기서 단순화를 위해서
θ: Momentum Thickness
로 적분 부분을 치환해주자.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-023.png)
두개의 drag force 방정식을 우리가 유도했으므로,
연립해주면 최종적으로 10번식
momentum integral relation 식.
즉, shear strss와 momentum thickness 미분식이 나온다.
(위식은 aminar turbulent 모두 만족)
자 여기까지, 우리는
boundary layer thickness를 구하기 위한
momentum thickness
momentum integral relation
을 유도하였다.
boundary layer thickness를 위해.
두번째 알아야 할 개념
b) Displacement Thickness, δ*
![Ch6 Boundary Layer theory part1 - thickness](./images/img-024.png)
left: boundary 내부 velocity profile
좌측 = 실제 boundary layer 내부 velcity profile (높이 = h)
우측 = free stream profile(Ue)라고 가정했을때 (높이 = h-δ*)
좌 우 상황의 높이 차이를
Displacement Thickness: δ*
라고 정의한다.
정의한후, 수식적으로 값을 구하는 것은 이지하다.
그냥 초록색 부분의 면적, 좌 = 우
라는 식을 세우면 된다.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-025.png)
그렇다면, 왜 굳이 저거를 정의했을까?? 라는 의문이 듣ㄴ다.
이유를 알기 위해
지금까지 다루었던 개념과 연결해보자.
stream line을 기준으로
Figure1
을 살펴보자.
1 -> 2로 control volume을 유체가 지나가는 상황이다.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-013.png)
Figure1. flat plate boundary layer w/ a stream line.
여기서 재밌는 사실은
Fig1 inlet(1번) 속도 profile = Fig2 오른쪽
Fig1 outlet(2번) 속도 profile = Fig2 왼쪽
![Ch6 Boundary Layer theory part1 - thickness](./images/img-024.png)
Figure2. right 속도장 높이 (h-δ*)
즉, stream line의 높이차이가 바로,
displacement thickness이라는 것이다.
즉, 유체가 viscous 효과로 인해서
원래 흐르든 것보다 위쪽으로 흐른다는 것을 알 수 있다.
그렇다면 정확히 어느정도 위쪽으로 흐르는지,
우리는 옆사진을 figure1을 보았지만, 실제로는
![Ch6 Boundary Layer theory part1 - thickness](./images/img-026.jpg)
위 그림처럼 면적만큼 위로 유체가 흐른다.
따라서, 이 면적을 계산하기 위해서
Displacement thickness를 정의하고 유도한다.
이제 진짜. Boundary layer thickness를 구해보자.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-023.png)
remind) momentum thickness
결국에 사실, u = u(y) velocity profile을 정의해야하는데,
굉장히 많은 실험적 정의가 진행되어 왔다.
예를들어 가장 흔히 쓰이는
flat plate velocity parabolic profile을 다음과 같이 정의하자.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-027.png)
정의한 Profile을 momentum thickness에 대입해주자.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-028.png)
그리고 이를 10번 momentum integral relation 식에 대입해주자.
(momentum thickness -> shear stress - 10번식)
![Ch6 Boundary Layer theory part1 - thickness](./images/img-029.png)
여기에서 shear stress - velocity관계식을 위해,
뉴턴유체 가정
을 더해주면
![Ch6 Boundary Layer theory part1 - thickness](./images/img-030.png)
이제 두 식을 연립해주고 적분 + BC을 적용시켜주면,
기가 막히게 우리가 원하던
Boundary layer thickness( δ) - x 관계식
이 도출된다.
![Ch6 Boundary Layer theory part1 - thickness](./images/img-031.png)
최종 displacement thickness - x 관계식.
속도장과
δ-x 관계식을 아는 상황에서,
Displacement thickness도 구할 수 있다( δ*)
![Ch6 Boundary Layer theory part1 - thickness](./images/img-032.png)

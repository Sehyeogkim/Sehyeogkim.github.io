---
title: "[Thermodynamics] Ch 6. The Inequality of Clausius & Entropy"
layout: single
author_profile: false
sidebar:
  nav: "docs"
source_url: "https://jeffdissel.tistory.com/67"
source_id: "67"
date: "2024-04-18T23:16:21+09:00"
category: "Thermodynamics"
---

Source: [https://jeffdissel.tistory.com/67](https://jeffdissel.tistory.com/67)

그림과 같이, Reversible cycle engine이 있다고 해보자.
![[Thermodynamics] Ch 6. The Inequality of Clausius & Entropy](./images/img-001.png)
우리는 이전 시간에, QH/QL = Th/TL 임을 확인 하였다.
(Ideal gas)
따라서,
![[Thermodynamics] Ch 6. The Inequality of Clausius & Entropy](./images/img-002.png)
반대로, Irreversible cycle
인 경우,
Qh 의 열을 동일하게 받았다고 했을때,
W irr < W rev
QL' (irr) > QL (rev)
따라서, QL이 커졌으므로,
![[Thermodynamics] Ch 6. The Inequality of Clausius & Entropy](./images/img-003.png)
결론적으로, reversible과 irreversible을 포함한 모든 cycle 에서
-> The Inequality of Clausius
![[Thermodynamics] Ch 6. The Inequality of Clausius & Entropy](./images/img-004.png)
------------------------------------------------------------------
자 이제 그림과 같이 State 1 <-> 2 이동하는
임의의
Reversible Process A,B,C
가 있다고 하자.
![[Thermodynamics] Ch 6. The Inequality of Clausius & Entropy](./images/img-005.png)
A-B cycle에서 전부 reversible이므로,
![[Thermodynamics] Ch 6. The Inequality of Clausius & Entropy](./images/img-006.png)
C-B cycle에서도 전부 reversible 이므로,
![[Thermodynamics] Ch 6. The Inequality of Clausius & Entropy](./images/img-007.png)
두 식을 연립하면,
![[Thermodynamics] Ch 6. The Inequality of Clausius & Entropy](./images/img-008.png)
이 식을 보고
'아하 moment'
가 떠오르게 된다.
경로에 상관없이
reversbile process path 안에서 dQ/T 는 동일 하다는 것이다.
따라서, 우리는 dQ/T를 Path independent thermodynamic property라고 할 수 있고,
'Entropy 의 변화량'
이라 부르고 다음과 같이 정의한다.
![[Thermodynamics] Ch 6. The Inequality of Clausius & Entropy](./images/img-009.png)
위 식을 적분해주면,
![[Thermodynamics] Ch 6. The Inequality of Clausius & Entropy](./images/img-010.png)
위식을 자세하게 들여다보면,
먼저, S2-S1은 경로와 무관한 값을 가질 것이다.
+
State 1 -> State 2로 가는 reversible 경로중 아무거나 하나를 적분해서,
위 식처럼 S2-S1을 구할 수 있다.
따라서,
Entropy는 h,u,p,T,v처럼
Thermodynamics property
라는 것,
u,h처럼, 우리는 s2-s1차이 값만 구할 수 있기 때문에,
reference point를 설정하고 표에 h,u,p,t,v 값들과 함께 표시되어 있다.
ex) reference point = 물의경우 삼중점, s = 0

---
title: "ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion"
layout: knowledge-home
source_url: "https://jeffdissel.tistory.com/m/162"
source_id: "162"
date: "2025-02-02T18:39:15+09:00"
category: "Continuum-Mechanics"
---

Source: [https://jeffdissel.tistory.com/m/162](https://jeffdissel.tistory.com/m/162)

ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion
이번 시간에는
Cauchy stress tensor에 대해서 자세하게
분석해보자.
가장 간결하게 보여주는 그림은 다음과 같다.
![ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion](./images/img-001.png)
저는 이렇게 이해했습니다.
traction vector(t)라는 것이, 각 면마다 작용하는데,
벡터이므로
, 각 면에서도 3가지 성분으로 쪼갤 수 있다.
여기서 면과 수직인 성분 - normal stress
면과 평행한 성분 - shear stress
임을 고체역학 시간에 다루었을 것이다.
![ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion](./images/img-002.jpg)
위를 보면 3가지 면의 total traction각각도 vector임을 알 수 있다.
여기서 stress tensor가 symmetric임을 증명해보자.
![ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion](./images/img-003.png)
점 A를 기준으로 Moment를 계산해보자.
![ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion](./images/img-004.png)
high order term -> 0 faster than the others.
관성모멘트도 High order term이므로, symmetrc함을 알 수 있다.
![ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion](./images/img-005.png)
1,2방향외에 2,3/ 1,3 방향으로 분석시 똑같은 결과가 나옴을 알 수 있다.
아주 중요.
Cauchy stress tensor - symmetric Matrix.
symmetric인게 왜 중요한가???
Part3에서도 다루었지만,
symmetric인 경우, 고유벡터3개를
기저벡터(서로 수직)으로 만들 수 있다.
![ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion](./images/img-006.png)

즉 좌표공간(새로운 기저벡터)로 변환시키면,
![ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion](./images/img-007.png)
에서
![ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion](./images/img-008.png)
Q: 고유벡터로 이루어진 행렬,(대각화과정)
로 변환시킬 수 있다.
변환후의 stress값이 최대,최소값이고,
principal stress라고 칭한다.
즉, 우리는 물체에 작용하는 최대 최소 응력을 계산할 수 있게 된다.
![ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion](./images/img-009.png)
여기서 sigma 11,22,33은
위 행렬의 eigen value값이기 때문에,
3*3행렬의 eigen value를 구해보면, 다음과 같다.
![ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion](./images/img-010.png)
____________
#Equations of motion
위에서 정의한 코시 stress tensor를 가지고,
힘의 평형 방정식을 작성해보자.
![ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion](./images/img-011.jpg)
t: traction vector
힘의 평형식을 세워주면,
Surface force + body force = m * a
![ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion](./images/img-012.jpg)
그리고 여기서, 우리는
![ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion](./images/img-013.jpg)
을 이용하여 좌항의 3성분들을 다음과 같이 변환할 수 있다.
![ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion](./images/img-014.jpg)
변환시킨 식을 대입후,
Δx1 Δx2 Δx3
를 좌항 우항 약분시켜주면 다음식이 유도된다.
![ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion](./images/img-015.jpg)
이후,
Δx -> 0 으로 수렴시키면 편미분 식으로 변환된다.
![ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion](./images/img-016.jpg)
여기서 우리가 이전 포스터에서와 위에서 정의한
Cauchy stress tensor로 traction vector를 정의한 후,
식에 대입해주자.
![ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion](./images/img-017.png)
최종적으로,
Cauchy's Equation of motion
이 도출된다.
위 식에서, Cauchy stress tensor = 압력, 점성력 항으로 구성되면,
유체역학의 Navier's Stokes Equations이 유도됨을 알 수 있다.
![ch2 Stress - part2 (σ, Cauchy stress tensor) , Equation of Motion](./images/img-018.jpg)
Navier's Stokes Equation.

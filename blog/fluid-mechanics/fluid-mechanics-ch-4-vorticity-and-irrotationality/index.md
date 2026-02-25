---
title: "[Fluid mechanics] Ch 4. Vorticity and Irrotationality"
layout: knowledge-home
source_url: "https://jeffdissel.tistory.com/m/38"
source_id: "38"
date: "2024-03-31T20:42:36+09:00"
category: "Fluid-Mechanics"
---

Source: [https://jeffdissel.tistory.com/m/38](https://jeffdissel.tistory.com/m/38)

[Fluid mechanics] Ch 4. Vorticity and Irrotationality
보통 회전이 없다고 많이 가정을 하고,
유체 문제에 접근한다.
하지만, 정확히 회전력, 회전에 관련된 유체의 움직임을 알 필요는 있다.
시작은 당연히,
회전 -> Angular velocity 부터 시작한다.
밑 그림과 같이 xy평면에서,
t초후에 A -> A', C-> C'으로 유체의 element가 움직였다고 가정하자.
![[Fluid mechanics] Ch 4. Vorticity and Irrotationality](./images/img-001.png)
![[Fluid mechanics] Ch 4. Vorticity and Irrotationality](./images/img-002.png)
그랬을때, 각속도는 z방향이고
시계반대방향을 양수라고 했을때, 각도 변화량의 평균값으로 나타낼 수 있다.
여기서 dt -> 0 으로 갈때, 단순한 삼각함수
d(alpha)와 d(beta)는 속도변화량으로 나타낼 수 있다.
![[Fluid mechanics] Ch 4. Vorticity and Irrotationality](./images/img-003.png)
따라서, 다시 각속도 식에 대입해주면, 다음과 같이 된다.
![[Fluid mechanics] Ch 4. Vorticity and Irrotationality](./images/img-004.png)
흠, 여기서 왜 이렇게 다시 정의한지는 모르겠지만, 아마 1/2가 귀찮아서 일듯 하다.
Vorticity는 그냥 1/2제거용으로, 다음과 같이 정의한다.
![[Fluid mechanics] Ch 4. Vorticity and Irrotationality](./images/img-005.png)
이제 정의한 Vorticity를 한번 신기하게 써보도록 하자.
먼저 Differential relations in Linear momentum Equation에서
![[Fluid mechanics] Ch 4. Vorticity and Irrotationality](./images/img-006.png)
여기서 마지막 항을 Vorticity를 이용해서 다음과 같이 바꿀 수 있다.
![[Fluid mechanics] Ch 4. Vorticity and Irrotationality](./images/img-007.png)
여기서 만약에 Irrotational 인 경우 Vorticity = 0 이라는 사실은 다 알것이다.
비회전유동이라 가정해주면,
![[Fluid mechanics] Ch 4. Vorticity and Irrotationality](./images/img-008.png)
Gradient항을 미분항으로 바꿔주기 위해서 양변에 dr(이동거리)를 내적해주자.
(g는 -z방향이라고 가정하여, 음수 붙혀줌)
![[Fluid mechanics] Ch 4. Vorticity and Irrotationality](./images/img-009.png)
여기서 이제 Steady flow라는 가정이 붙혀지면?? 우리가 아는 베르누이가 나온다.
![[Fluid mechanics] Ch 4. Vorticity and Irrotationality](./images/img-010.png)
-------------------------------------------------------------------------
다음 Vorticity를 색다르고 유용하게 사용해보자.
먼저, Helmholtz decomposition에 대해서 알고 들어가보자.
![[Fluid mechanics] Ch 4. Vorticity and Irrotationality](./images/img-011.png)
(A는 divergence가 0 인 백터필드이고,
ϕ는 scalar 함수이다)
즉, 어떤 백터를 발산백터, curl백터 이 두가지로 분해 할 수 있단 말이다.
따라서, 만약에 Curl(V) = 0이라면, 저 식에서 발산 term만 남게 된다.
∇ ×
A =
0 이라는 말이다.
따라서, V=∇ϕ
다시 정리하면
If ∇ × V = 0 then, V=∇ϕ
여기서 ϕ= ϕ(x,y,z,t) is called the 'Velocity potential function'
V=∇ϕ 이므로,
u =
∂ x/ ∂ ϕ, v = ∂ y/ ∂ ϕ,
w = ∂ z/ ∂ ϕ
그리고 Incompressible continutiy eq에서는
![[Fluid mechanics] Ch 4. Vorticity and Irrotationality](./images/img-012.png)
위와 같이 Laplace eq.이 derive된다.

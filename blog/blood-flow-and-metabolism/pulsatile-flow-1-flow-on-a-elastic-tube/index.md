---
title: "[Pulsatile flow] 1. Flow on a elastic tube"
layout: knowledge-home
source_url: "https://jeffdissel.tistory.com/m/123"
source_id: "123"
date: "2024-11-03T12:10:59+09:00"
category: "Blood-Flow-and-Metabolism"
---

Source: [https://jeffdissel.tistory.com/m/123](https://jeffdissel.tistory.com/m/123)

[Pulsatile flow] 1. Flow on a elastic tube
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-001.png)
(위): Rigid wall, (아래): Elastic wall.
혈관의 흐름을 분석하기 위해서,
실제 혈관의 벽면의 움직임도 고려해 주어야 한다.
이전 포스터에서는 혈관 벽이 고정 rigid wall
가정으로 혈액의 속도장을 계산하였다면,
(사실 큰 동맥 이외에는 벽의 움직임이 크게 없다.)
이번에는,
혈관 벽이 linear 한 elasticity
를 가진다고 가정을 하고
혈액의 속도장을 유도해보자.
시작은
Axissymmetric,
Cylindrical Coordinate
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-002.png)
Navier's Stokes equation(모멘텀 보존 방정식)
Conservation Equation
으로 시작한다.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-003.png)
여기서 핵심은 rigid wall 과 다르게
r 방향의 속도 : v 가 일정하지 않다는 것이다.
따라서, 우리가 유도할 u,v,p는
전부 x,r,t를 variable로 가지고 있다.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-004.png)
For simplicity
두가지 가정을 추가해주자.
심장박동에 의한 파동의 속도 : c
유체의 평균속도 : u_hat
파동의 파장: L
벽면의 두께: a
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-005.png)
바로 파동의 파장이 벽면의 두께보다 훨씬 두껍고,
파동의 이동속도가 유체의 평균속도 보다 훨씬 크다는 가정이다.
쉽게말해,
위 유동은 두가지 파동이 존재한다.
첫번째 심장의 박동에 따른 x방향의 진동
두번째, 벽면의 탄성에 의한 r방향의 진동
두께가 굉장히 얇고 x방향의 파동의 파장이 굉장히 크다고 가정하면,
결국, r방향의 속도 변화가 x방향의 속도 변화보다 dominant할 것이다
(radius < L)
더불어, 유체는 공간에 대해서 보다 시간에 대해서
속도가 더 클것이다.(파동의 속도가 크기 때문에)
따라서, 위 가정을 모멘텀 보존, 연속방정식에 대입해주면,
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-006.png)
여기서 짚고 넘어가야 할 것은,
벽면의 진동,
심장 박동에 의한 진동,
이 두가지가 sinousal 한 파동함수를 만들고,
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-007.png)
이를 수학적으로 표현하면,
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-008.png)
위 x,t,에 따른 진동의 식을 그대로
모멘텀보존, 연속방정식에 대입해주자.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-009.png)
이전 rigid wall에서도 했던 방식 그대로,
우리는 위 식을 Bessel function 로 바꾸기 위해서,
(우리는 베셀함수의 해를 이미 알고 있으므로)
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-010.png)
다음 4,5,6식이 도출된다.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-011.png)
여기서, 4,5번 식을 보면 inhomogeneous Bessel Equation임을 알 수 있다.
(
Bessel equation 무조건 알아야합니다...)
https://jeffdissel.tistory.com/101
Bessel's Equation_Part1
심장박동의 Pulsatile Flow 의 유동해석(주기적으로 움직이는 심박에 의한)(혈액 속도장 계산) 과정속에서, 뜬금없이 Bessel function이 등장해버렸다. 이 친구는 학부시절,열전달 (전도) 시간에
jeffdissel.tistory.com
bessel 함수 해를 구하기 전에,
boundary condition을 확인해주자.
no-slip condition - > 벽에서 속도 = 0
(r = a 일때, U = V = 0)
그리고, r =0 일때 속도는 유한한 수이어야 한다.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-012.png)
먼저 4번 식의 경우
homogenoeus bessel equation의
m = 0 정수 이므로,
일반해는 1차 제1,2, 베셀 함수로 표현된다(J0(x), Y0(x))
여기에 inhomogeneous equation의 해
specific solution : yp_1
이라고 하자.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-013.png)
boundary condition을 적용시키면
r = 0 일때 Y0(0) = - infinity 이므로, C2 = 0 이 되어,
J0(ζ) , yp_1(ζ) 로만 일반해는 표현된다.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-014.png)
Second kind of bessel function.
같은 방식으로 5번 inhomogeneous bessel equation의 해 유도해보자.
m = 1 일때의 베셀 함수,
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-015.png)
똑같이 BC 를 적용시켜부면 C4 =0 이 되어,
일반해는 J1(ζ), yp_2(ζ)로 구성됨을 알 수 있다.
여기서, bessel 함수의 특수해를
기존 Bessel 함수의 선형형태로 가정
을 해보자.
(베셀함수의 적분과 미분 - 베셀함수의 선형형태이므로)
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-016.png)
지금부터는 가정한 해의
상수 l,m
을 찾기 위하여,
모멘텀보존, 연속방정식으로부터 유도한 4,5,6 방정식에 각각 대입해주자.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-017.png)
자 먼저, 가정한 yp_1을 대입해보자.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-018.png)
= 4번 식 * ζ^2
위 4번 식의 특수해 이므로, 대입해주면,
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-019.png)
위 식을 정리 하기 위해서 치환해주자.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-020.png)
치환을 해주면, 베셀함수의 정의에 의하여,
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-021.png)
따라서, 최종적으로 7번 식이 유도된다.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-022.png)
같은 방식으로 yp_2은 5번 비동차 베셀 방정식의 특수해이므로,
가정한 형태로 대입해주자.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-023.png)
위와 같은 방식으로 치환후 전개해주면 8번식이 도출된다.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-024.png)
지금까지, 4,5 식에 대입하였고, 이번에 6번 식에 대입해보자.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-017.png)
6번 방정식은
베셀 방정식이 아니기 때문에, 일반해의 형태로 대입해 주어야 한다
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-025.png)
yp_1 , yp_2 특수해들을 선형형태로 가정한 일반해.
그대로,
6번식(연속방정식)
에 대입해주면
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-026.png)
위 식을 정리하기 위해서, 베셀함수의 성질을 사용하자.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-027.png)
그대로 9번 식에 대입후
ζ
를 곱해주면,
감사하게 소거항이 생긴다.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-028.png)
좌항 모든 부분에
ζ
가 있기 때문에 나누어주자.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-029.png)
여기서 모두 1차 베셀함수 m= 0 인 경우이므로,
전부 무한 급수로 표현 해 줄 수 있다.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-030.png)
m = 0, 제1차 베셀함수의 해
바로 위 식에 대입해주면,
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-031.png)
위 식 = 0을 만족하기 위해서는 n -> 무한까지 가기 때문에
m/2 = l/2 를 만족해야만 한다.
더불어, 각 항의 계수들도 모두 동일 해야만 함을 알 수 있다.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-032.png)
위 정보를 가지고, 아까 4,5번 방정식(모멘텀보존 방정식)에
대입후 유도하였던 7,8번 식을 다시 살펴보자.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-033.png)
자세히 보면, 7번 방정식을
ζ
로 미분한 방정식이 8번 방정식이므로,
이를 통해 12번 방정식을 도출할 수 있다.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-034.png)
12번 방정식에
우리가 10번 방정식에서 구한 계수 관계를 대입하자
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-035.png)
여기서, 베셀 함수의 성질을 그대로 대입해주면,
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-036.png)
다음과 같이 유도된다.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-037.png)
이후 정리해주면 우리는 드디어
우리의 목적인 m 을 유도할 수 있다.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-038.png)
이제 우리는 특수해가 어떻게 생겼는지를 알기 때문에,
그대로 구한 l=m을 대입해주어서,
U,V,P를 나타내보자.
먼저 그대로 7번 식에 대입해주어 P를 구해보자.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-039.png)
이제 계수들을 정리하기 위해서,
아까 6번 연속방정식에 U,V를 대입하고 유도하였던,
계수 관계를 살펴보자.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-032.png)
우리가 구한.m을 대입해주면,
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-040.png)
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-041.png)
이제 위 속도 관계식에
l,m, 계수들을 대입해주자.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-042.png)
진짜 마지막으로 깔끔하게 정리하기 위해서,(계수들을)
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-043.png)
다음과 같이 정리 할 수 있다.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-044.png)
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-045.png)
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-044.png)
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-045.png)
최종적으로 우리는 베셀함수를 통해서,
elastic tube wall + pulatile flow의 경우에
속도장이 어떻게 바뀌는 지를 다음과 같이 유도하였다.
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-046.png)
찐찐막으로 우리는 t,x에 따른 주기함수형태였으므로,
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-047.png)
최종 일반해는,
![[Pulsatile flow] 1. Flow on a elastic tube](./images/img-048.png)

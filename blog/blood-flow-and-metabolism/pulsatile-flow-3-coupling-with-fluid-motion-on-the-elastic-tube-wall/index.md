---
title: "[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall"
layout: knowledge-home
source_url: "https://jeffdissel.tistory.com/125"
source_id: "125"
date: "2024-11-17T17:02:30+09:00"
category: "Blood-Flow-and-Metabolism"
---

Source: [https://jeffdissel.tistory.com/125](https://jeffdissel.tistory.com/125)

지금 우리는
Pulsatile flow
Elastic thin tube에서
유체와 고체의 변형을 고려한
유체의 유동에 대해서 분석하고자 한다.
지지난 포스터에서
어렵게 유체의 속도와 압력을 유도하였고,
https://jeffdissel.tistory.com/123
[Pulsatile flow] Flow on a elastic tube
혈관의 흐름을 분석하기 위해서,실제 혈관의 벽면의 움직임도 고려해 주어야 한다. 이전 포스터에서는 혈관 벽이 고정 rigid wall가정으로 혈액의 속도장을 계산하였다면,(사실 큰 동맥 이외에
jeffdissel.tistory.com
지난포스터에서
고체의 변형과 shear stress, pressure 관계식을
https://jeffdissel.tistory.com/124
[Pulsatile flow] 2. Force on the elastic tube wall
지난 포스터에서 우리는,https://jeffdissel.tistory.com/123 [Pulsatile flow] Flow on a elastic tube혈관의 흐름을 분석하기 위해서,실제 혈관의 벽면의 움직임도 고려해 주어야 한다. 이전 포스터에서는 혈관
jeffdissel.tistory.com
다음과 같이 유도하였다.
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-001.png)
먼저 유체의 압력은 우리가 지지난 포스터에서 이미
유도한 그대로 대입할 예정이다.
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-002.png)
이제 두번째로
Shear stress를 유체의 성질로 표현해보자.
no-slip bc, axissymetric으로 인해
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-003.png)
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-004.png)
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-005.png)
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-004.png)
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-005.png)
shear stress는 13번 식으로 표현 할 수 있다.
여기에 우리가 지지난 포스터에서 구한
베셀함수로 표현한 속도를 13번 식에 대입해주자.
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-006.png)
여기에 베셀함수 성질그리고,
r=a일때를 우리는 구하고 있기 때문에,
이를 이용하여, 1번항은 다음과 같이 정리된다.
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-007.png)
2번식 정리를 위해 우리가 정의하였었던,
(유체 속도식 유도를 위하여)
오메가, 람다를 remind 하고 들어가자.
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-008.png)
+ 감마 = iwa/c - 0 으로 근사하며,
(파동의 파장 >> 튜브 반지름)
이때 베셀함수의 성질로 다음과 같이 정리 정리된다.
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-009.png)
자 위 도구들을 가지고 2번식을 정리해보자.
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-010.png)
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-011.png)
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-010.png)
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-011.png)
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-012.png)
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-013.png)
위 식의 마지막 과정은 다음의 가정의 포함되어 있습니다.
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-014.png)
최종적으로,
우리가 정리한 1,2번식을 이용하여 새로운 shear stress 방정식 13을
다음과 같이 나타낼 수 있다.
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-015.png)
지난 포스터에서 유도한
고체 변위 stress 식 10,11에
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-016.png)
유체 shear stress, pressure 식 12,13을 대입해보자.
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-017.png)
최종적으로 구한 14,15 식은
유체의 property(밀도, pusatile flow의 진동수)와
시공간에 따른 고체의 Displacement 의 관계식이다.
__________________
여기서 이제 우리는 고체 유체 Surface
Boundary condition을 생각해보자.
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-018.png)
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-019.png)
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-018.png)
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-019.png)
첫번째 식의 의미는
유체의 벽면에서의 속도 =
고체의 element의 시간에 따른 변위
(고체와 유체 surface)
두번째 식의 의미는
유체와 고체가 surface에서 만나므로,
결국 벽면의 변위도 유체와 같은 진동수를 가지고 진동.
(하지만 중요한 것은 유체와 진동수는 동일하지만,
같은 phase의 운동은 아니다)
(저도 처음에 무슨 말이야 이게? 라고 생각을 했지만
이 부분을 고민하시면서 계속 블로그를 보시면
해답이 나올 겁니다 ㅎㅎ)
아무튼, 위에서
두번째 가정
을
14번 식에 먼저 대입해주자.
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-020.png)
이후 정리해주면 밑의 16번식이 도출된다.
같은 방법으로 15번식 +
두번째 가정
-> 17번 식
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-021.png)
이제
첫번째 가정 + 두번째 가정
을 통해
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-022.png)
여기서 유체의 속도를
계속해서 나오는
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-023.png)
파동의 파장(L) >> 반지름 가정(a)
r=a에서의 속도는 다음과 같이 유도되었다.
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-024.png)
위 속도장을 BC1,2 식에 대입해주면 18,19 식이 유도된다.
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-025.png)
자 여기서, 16 17번식을 파장>>반지름 가정을 통해서,
정리할 수 있다.
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-026.png)
16번 식 우항2번째 정리 -> 16'식 유도
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-027.png)
17번 식 정리 -> 17'식
최종적으로 우리는 A,B,D,F 상수 4개를 위한 식을
Boundary condition으로 유도하였다.
![[Pulsatile flow] 3. Coupling with Fluid motion on the elastic tube wall](./images/img-028.png)
자 다음포스터에서 위의 계수 4개 방정식 4개이므로,
연립방정식의 해를 구해보자.

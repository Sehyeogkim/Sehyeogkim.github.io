---
title: "Ch1 Kinematics-part3 - Strain tensor(E*, E)"
layout: knowledge-home
source_url: "https://jeffdissel.tistory.com/157"
source_id: "157"
date: "2025-01-31T18:00:52+09:00"
category: "Continuum-Mechanics"
---

Source: [https://jeffdissel.tistory.com/157](https://jeffdissel.tistory.com/157)

지난 시간에 Deformation Gradient Tensor(F),
Cauchy Green tensor(C,B)에 대해서 분석해보았다.
이번에는 strain tensor즉. 길이변화에 관한 tensor들을 정의해보자.
![Ch1 Kinematics-part3 - Strain tensor(E*, E)](./images/img-001.png)
지금까지 정의한 relationships.
- dx = F dX
- F = I + ∇u
- F = RU = UV
- C = F^T F = U^2
- u(X,t) = x(X,t) - X
1. Lagrangian Strain Tensor(E*)
C의 F를 정의대로 전개해준 후,
E* 을
Lagrangian Strain tensor
로 정의한다.
![Ch1 Kinematics-part3 - Strain tensor(E*, E)](./images/img-002.jpg)
이렇게 정의한 이유를 tensor의
물리적 의미로 살펴보자.
![Ch1 Kinematics-part3 - Strain tensor(E*, E)](./images/img-003.png)
![Ch1 Kinematics-part3 - Strain tensor(E*, E)](./images/img-004.jpg)
변형전 후, 임의의 내부벡터(1),(2)
dx = F dX, C = F^T F 임을 이용하면.
![Ch1 Kinematics-part3 - Strain tensor(E*, E)](./images/img-005.jpg)
여기서 먼저 E의 diagonal term을 살펴 보기 위해서,
(1) 과 (2)가 같은 방향이라고 가정하자.
![Ch1 Kinematics-part3 - Strain tensor(E*, E)](./images/img-006.jpg)
Strain의 개념은 길이의 변화량 / 초기 길이 임을 감안하면,
위의 정의가 strain으로써 가능함을 알 수 있다.
이제 off-diagonal term을 살펴보기 위해,
변형전 (1),(2)가 수직이었다고 가정하자.
![Ch1 Kinematics-part3 - Strain tensor(E*, E)](./images/img-007.jpg)
2. Infinitesimal Strain tensor (E)
![Ch1 Kinematics-part3 - Strain tensor(E*, E)](./images/img-008.png)
여기 에서
아주 작은 변형이라는 가정
을 추가해주면,
high order term을 소거해줄 수 있다.
![Ch1 Kinematics-part3 - Strain tensor(E*, E)](./images/img-009.jpg)
![Ch1 Kinematics-part3 - Strain tensor(E*, E)](./images/img-010.png)
3*3 Infintesimal Tensor.
정확히 항들의 의미를 분석하기 위해서,
Diagonal term, off-diagonal term들을 살펴보자.
![Ch1 Kinematics-part3 - Strain tensor(E*, E)](./images/img-004.jpg)
변형전 후, 임의의 내부벡터(1),(2)
길이 변화를 살펴보기 위한 방법은 내적이 최고이다.
![Ch1 Kinematics-part3 - Strain tensor(E*, E)](./images/img-011.jpg)
#Diagonal Term of E
![Ch1 Kinematics-part3 - Strain tensor(E*, E)](./images/img-012.jpg)
즉, E tensor의 diagonal term은
고체역학 시간에 우리가 배운 정의인,
Normal strain
을 뜻한다.
#Off diagonal Term of E.
![Ch1 Kinematics-part3 - Strain tensor(E*, E)](./images/img-013.jpg)
shear strain/2 = Emn
즉, off diagonal term임을 위와 같이 증명할 수 있다.
다시 말하면, Shear strain의 경우 대칭이므로,
ex) r12 = r21
따라서, Eij = Eji 즉 Symmetric Tensor임을 가볍게 알 수 있다.
선형대수학 시간에 배웠겠지만,
symmetric Tensor
인 경우 아주 중요하고
대단한 특징이 존재한다.
1. 3개의 직교한 고유벡터가 존재.
2. 3개의 실수인 고유값 존재.
-> E 대각화 가능.
대각화가 가능하다는 말을 정확히 다시 표현하면,
변형전 coordinate의 기저벡터(1,2,3)들을
E의 Eigen vector(n1,n2,n3)로 바꾸게 되면,
shear strain = 0 이 되는
diagonalized E
로 바꿀 수 있다는 말이다.
![Ch1 Kinematics-part3 - Strain tensor(E*, E)](./images/img-014.jpg)
![Ch1 Kinematics-part3 - Strain tensor(E*, E)](./images/img-015.jpg)
Diagonalized E
그리고, 고유값 분해를 통해서
우리는 이 대각화된 E의 대각성분(E1,E2,E3)는
사실 기존 E의 고유값임을 알 수 있다.
E1,E2,E3 are called 'Principal Strain'
여기서 고유값을 찾기위해서
det(E- λ I ) = 0
전개하면, 다음과 같이 3차방정식이 나온다.
그리고 3차방정식의 계수들을 I1,I2,I3로 표기하자.
![Ch1 Kinematics-part3 - Strain tensor(E*, E)](./images/img-016.jpg)
여기서의 계수들을 Invariants 1,2,3로 위와같이 정의하고,
추후에 아주아주아주 중요하게 쓰인다.
___ ___ ___ ___ ___ ___
지금까지 Strain tensor 두가지
1. Lagrangian Strain tensor(Large deformation, E*)
2. Infintesimal Strain tenesor(small deformation, E)
에 대해서 알아보았다.
![Ch1 Kinematics-part3 - Strain tensor(E*, E)](./images/img-017.jpg)
#E
small deformation가정의 경우 strain이 굉장히
간결하게 표현되고, 고체역학에서 배웠던
normal shear strain과 동일함을 확인할 수 있었다.
#E*
먼저, E*의 경우 E보다 더 정확한 값임은 당연하다.
(high order term 포함)
또한, FTF = U^2의 경우,
rotation이 제외된 순수한 stretching을 의미하며
아무것도 stretch 되지 않는 상태인 I로 뺀 값을 strain으로 갖는다.
그리고 무엇보다. F로 표현되기 때문에
(F: Material, Larangian
description)
즉, 변형전 좌표계에서 살펴본 strain값이므로
더 정확하다고 말할 수 있다.

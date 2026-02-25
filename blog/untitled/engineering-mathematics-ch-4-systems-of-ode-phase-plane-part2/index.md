---
title: "[Engineering Mathematics] Ch 4. Systems of ODE, Phase plane - part2"
layout: single
author_profile: false
sidebar:
  nav: "docs"
source_url: "https://jeffdissel.tistory.com/m/51"
source_id: "51"
date: "2024-04-10T13:49:34+09:00"
category: "과학"
---

Source: [https://jeffdissel.tistory.com/m/51](https://jeffdissel.tistory.com/m/51)

[Engineering Mathematics] Ch 4. Systems of ODE, Phase plane - part2
2x2 matrix 인 Linear homogeneous ODE system 을 살펴보자.
![[Engineering Mathematics] Ch 4. Systems of ODE, Phase plane - part2](./images/img-001.png)
지난 시간에 배운 방법으로 y = xe^( λt) 라고 가정 후, 대입해주면,
![[Engineering Mathematics] Ch 4. Systems of ODE, Phase plane - part2](./images/img-002.png)
Eigen vector value 문제로 바뀌게 된다.
위 식이 만족하기 위해서는, determinatn of (A-
λI) = 0 이어야 했다.
![[Engineering Mathematics] Ch 4. Systems of ODE, Phase plane - part2](./images/img-003.png)
마지막 방정식의 계수를 치환해주면,
![[Engineering Mathematics] Ch 4. Systems of ODE, Phase plane - part2](./images/img-004.png)
두식을 연립해주면
![[Engineering Mathematics] Ch 4. Systems of ODE, Phase plane - part2](./images/img-005.png)
사실 지금까지, 이 과정을 한 이유는
여기서, p,q,△로 Critical point의 종류가 어떤지를 수학자들은 Table로 정리하였다.
![[Engineering Mathematics] Ch 4. Systems of ODE, Phase plane - part2](./images/img-006.png)
그리고 이렇게 Critial point, phase plane , cirticial point종류를 나눈 이유는 사실.
Stability
때문이었다.
stability는 단순하게 시간이 흐름에 따라서, 해가 적정한 선에서 계속 유지된는가?
아니면 불안정하여 발산해 버리나??? 이다.
어쩌면, 해가 적정한 선에서 계속 유지되다가 Critical point로 전부 수렴해버리는 경우도 존재할 것이다.
따라서, 위 언급한 종류를
1. Stable, 2. Unstable 3. Stable and attractive 라고 정의한다.
수학자들은 참 대단하긴 하다, 뭔가 추상적으로 말로 써봤는데 이것을
뭔가 수식적으로 표현 해야하니까 어려운 것 같다.
![[Engineering Mathematics] Ch 4. Systems of ODE, Phase plane - part2](./images/img-007.png)
![[Engineering Mathematics] Ch 4. Systems of ODE, Phase plane - part2](./images/img-008.png)
그리고 p,q,△ 에 따라서 table로 정리하였다.
![[Engineering Mathematics] Ch 4. Systems of ODE, Phase plane - part2](./images/img-009.png)
-------------------------------------------------------------------------------------------------------------------

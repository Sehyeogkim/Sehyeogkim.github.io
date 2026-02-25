---
title: "Anomaly Detection"
layout: single
author_profile: false
sidebar:
  nav: "docs"
source_url: "https://jeffdissel.tistory.com/m/142"
source_id: "142"
date: "2024-12-11T15:45:20+09:00"
category: "Deep-learning"
---

Source: [https://jeffdissel.tistory.com/m/142](https://jeffdissel.tistory.com/m/142)

Anomaly Detection
Anomaly detection이란,
수많은 데이터들 중에서
비정상적인 녀석들
을 구분해내는 것이다.
![Anomaly Detection](./images/img-001.jpg)
비정상적인 빨간 달걀
구분하는 방법은
분류작업을 통해서,
아래 왼쪽처럼, 다른 Group으로 표시할 수도 있고,
아래 오른쪽처럼, 비정상적인 값을 확인하고 구분할 수도 있다.
![Anomaly Detection](./images/img-002.png)
결론적으로 우리는,
우리가 가지고 있는 데이터들에
라벨
을 부여할 수 있고,
Anomaly - label
비정상의 정도를
점수
로 나타낼 수도 있다.
Anomaly - score
이를 통계적으로 분류하는 작업이 가장 대중적이지만,
group이 많아지거나, 고차원 space로 갈 경우
굉장히 복잡해진다는 단점이 존재한다.
![Anomaly Detection](./images/img-003.png)
따라서, 지금 까지 배운 deep learning model을
사용해보자.
1.CAE - Anomaly detection
이렇게 7로 학습한 CAE model이 있다고 가정해보자.
![Anomaly Detection](./images/img-004.png)
정상데이터(위 예시에서 7로)
모두 학습되고 나서,
판별을 위해,
![Anomaly Detection](./images/img-005.png)
정상데이터(7), 비정상데이터(5)
를 모델에 짚어 넣어 보자.
밑의 결과처럼,
normal data(7) 의 경우 7과 비슷하게 나오지만,
Anomaly data의 경우 굉장히 7과 벗어난(가운데 선이 생김)
결과 나옴을 알 수 있다.
![Anomaly Detection](./images/img-006.png)
따라서, 우리는 input data와 reconstructed data의 차이가 굉장히 큰 녀석은
abnomaly data이다 라고 판단할 수 있다.
![Anomaly Detection](./images/img-007.png)
결국, 우리는 error의 threshold를 정의하고,
그에 따라서 abnomaly 인지 normal인지 구분해주면 된다.
![Anomaly Detection](./images/img-008.png)
(요약: 시작은 정상데이터로 학습시킨후,
판별을 위한 데이터를 짚어 넣는다)
2. AnoGAN - Anomaly detection GAN
이번에는 GAN을 이용해보자.
![Anomaly Detection](./images/img-009.png)
1. 먼저
normal data 즉, 정상데이터
로 generator, discriminator를 학습시킨다.
2. 이후 우리가 정상인지 비정상인지 구분하고 싶은
데이터
를 가지고 온다.
3. 그리고 그 데이터(정상or비정상)을 Generator가 잘 아웃풋 할 수 있는
(z)
를 찾는다.
z: Noise(Latent Space value)
![Anomaly Detection](./images/img-010.png)
z찾는 과정.
4. 찾았으면, 해당 z를 GAN에 input으로 넣고,
error를 계산한다.
만약에 z가 정상데이터 였다면, discriminator가 진짜와 가짜를 잘 구분하지 못할 것이다.
하지만 반대로, z가 비정상데이터였으면, 정상으로 학습한 discriminator는 진짜와 가짜를 쉽게 구분할 것이다.
따라서, Discriminator가 진짜 가짜를 구분하는 정도를 기준으로
데이터가 정상인지 비정상인지를 구분할 수 있다.
3. f-AnoGAN - fast Anomaly detection GAN
위의 GAN anomaly detection에서 딱 봐도,
어색하고 한가지 오래걸릴 것처럼 생긴 작업이 있다.
바로, z를 찾는 과정 이다.
이를 완전 쉽게 빠르게 하기 위해서 탄생한 것이 바로
f-AnoGAN
즉, noise 부터 GAN을 시작하지 않고,
앞에 encoder를 장착하여
실제 사진으로부터 시작하도록 GAN을 설계한다.
![Anomaly Detection](./images/img-011.png)
이를 경우, z를 자동으로 학습하면서 바로 찾을 수 있게 된다.
위 모델을 예시로,
2- 정상
6 - 비정상
이라고 가정하자.
먼저
f-AnoGAN
을 2(정상데이터)로 학습시킨다.
이후에, 비정상데이터를 넣게 되면,
생성된 이미지는 discriminator를 속이기 쉽지 않을 것이다.
![Anomaly Detection](./images/img-012.png)

---
title: "Pre-trained Model & Transfer Learning"
layout: single
author_profile: false
sidebar:
  nav: "docs"
source_url: "https://jeffdissel.tistory.com/138"
source_id: "138"
date: "2024-12-11T12:36:22+09:00"
category: "Deep-learning"
---

Source: [https://jeffdissel.tistory.com/138](https://jeffdissel.tistory.com/138)

[Pre-trained Model]
굉장히 거대한,
model을 새롭게 학습시키고,
구조화 시키는데 수많은 시간이 들어간다.
따라서, 사용 목적이 다르더라도
기존의 학습된 거대한 모델(pre trained model)을
가져와서 사용하는 방식이 바로
Transfer Learning 이다.
그렇다면,
기존의 학습된 거대한 모델에는
어떠한 것들이 있는지 살펴보자.
1. LeNET
![Pre-trained Model & Transfer Learning](./images/img-001.png)
지금까지 쓰이는 CNN 모델의 구조의
basic component를 알려주는
전통적인 모델이다.
보이는 것처럼 기본적으로,
convolutional filter수를 늘리고,
feature map size를 줄인후,
마지막에 flatten작업으로
ANN구조로 원하는 output을 도출하도록 한다.
2. Alex Net
![Pre-trained Model & Transfer Learning](./images/img-002.png)
lenet에 더하여, dropout, data augmentation등
추가적인 방법들을 더한 모델이다.
3. VGG
![Pre-trained Model & Transfer Learning](./images/img-003.png)
위 모델들보다 훨씬 깊은 구조로,
모델이 structure되어 있음을 알 수 있다.
-> 더더욱 깊은 feature을 추출하기 위함.
'very deep model'
4. Google net/ Inception
![Pre-trained Model & Transfer Learning](./images/img-004.png)
아주 신기하게,
kernel size를 다양하게 병렬적으로 filter 작업을 수행한다.
이를 통해 다양한 사이즈에서의 feature들을 학습하고,
마지막에 filter concatenation에서
전체 특징을 합쳐주는 작업을 진행한다.
(다른 모델들 보다, feautre 추출에 힘을 씀)
feature의 추출이 중요한
image segmentation 분야에서
많이 쓰인다.
5. Res-Net
![Pre-trained Model & Transfer Learning](./images/img-005.png)
x: input
F(x): convBlock 결과
H(x) : output
= F(x) + x
굉장히 많이 쓰이는 모델 구조이다.
위 사진은 R-Net의 한 convBlock인데,
한 블락에서 Input을 마지막에 다시 가져와서 더해준다.
핵심 적인 것은 결국,
학습 과정에서 weight는 업데이트 되고,
F(x)를 통해서 결국 계속해서 학습된다는 것이다.
재밌는 사실은
ouput - input = F(x)
이므로 residual = F(X)
따라서, residual 을 학습한다라고 하여
Res-net
6. Dense net
![Pre-trained Model & Transfer Learning](./images/img-006.png)
이전의 Res-net은
한 block의 input을 같은 block의 ouput에 더해주었다면,
Dense Net은
다른 블락에게도 전달해주는 구조이다.
굉장히 복잡하지만,
이전 정보들을 모두 함축할 . 수 있다.
CNN에서 이전정보라 함은
Spatial information이므로
Spatial information이 중요한
작업에 쓰인다.
7. U-Net
![Pre-trained Model & Transfer Learning](./images/img-007.png)
Convolutional Auto Encoder(CAE)
의 구조를 띠는 U-Net은
실제로 medical image 분류에 많이 쓰이는 모델이다.
다음 포스터에서 CAE에 대해서 자세하게 다루겠지만,
autoencoder처럼
Encoder(사진축소) : 사진의 feautre를 추출
Decoder(사진 복원): Feature로 부터 사진 제작.
핵심은 Encoder부분에서와 Decoder에서의 부분을
연결시켜 주어. 이전 정보를 최대한 복원하는 방식을 사용한다.
(Skip connection)
지금까지 pre-trained model들에 대해서 알아보았고,
이것을 실제로 사용하는 방법은 매우 간단하다.
그냥 tensorflow로 import하면 된다.
![Pre-trained Model & Transfer Learning](./images/img-008.png)
![Pre-trained Model & Transfer Learning](./images/img-009.png)
![Pre-trained Model & Transfer Learning](./images/img-008.png)
![Pre-trained Model & Transfer Learning](./images/img-009.png)
pretrained에서 가져온 model
[Transfer Learing]
위의 학습된 모델을 가지고,
결국 우리가 원하는 task를 위한 output을 위해서
뒷부분만 수정해주고 학습시키면 된다.
![Pre-trained Model & Transfer Learning](./images/img-010.png)
즉, 좌측의 source data로 이미 학습된 모델이 존재할때,
우리가 원하는 target data, 로 원하는 target model은
중간 later-weight을 모두 복사하고,
마지막의 output layer만 수정하고 학습시키면 된다.
![Pre-trained Model & Transfer Learning](./images/img-011.png)
이게 가능한 이유는,
결국에 중간 layer들은
특징을 추출하는 층이다.
사진의 특징이라하면,
edge, boundary, 등등
공통적인 범위안에 존재한다.
따라서, 최종 task가 달라지더라도,
결국 추출해야하는 특징은 비슷하거나 동일하다는 것이다.

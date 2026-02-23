---
layout: post
title: "Agentic AI 구조 part2 - framework"
date: 2026-02-23
author: Jeff
categories: [theory, agentic-ai]
---


Agentic AI를 한 문장으로 정리하면, **사용자 의도를 이해하고 → 여러 단계 계획을 세우고 → 도구를 호출해 실행까지 끝내는** 자율 시스템이다.
단순히 “답변을 생성하는 모델”이 아니라, **계획(Planning)** 과 **도구(Tools)** 를 통해 실제 업무를 완료하도록 설계된 아키텍처인 것.

---

## 0. Agentic AI 아키텍처를 구성하는 큰 블록들

Google Cloud 문서에서 정의한, 에이전트 시스템 요소들.

- **Frontend framework**: 사용자가 대화/작업을 요청하는 UI
- **Agent development framework**: 에이전트 로직(루프, 상태, 도구 연결)을 만드는 프레임워크
- Agent tools: 검색, DB, 사내 API 등 “행동”을 수행하는 도구 묶음
- Agent memory: 대화/세션 상태와 장기 기억 저장
- Agent design patterns: 싱글 에이전트 vs 멀티 에이전트 등 구조 패턴
- Agent runtime: 에이전트 애플리케이션이 실제로 돌아가는 실행 환경
- AI models: 추론/의사결정 엔진(LLM 등)
- Model runtime: 모델을 서빙하는 인프라(관리형 API/컨테이너/GKE 등)

여기서 오늘의 주제는 이 중에서도 frameworks에 대해서 이야기 해보자.

![Agentic AI 아키텍처](images2/agentic_ai_structure.svg)


## 1) Frontend framework: 사용자가 에이전트를 ‘쓸 수 있게 만드는 층’

Google Cloud 문서에서 정의한 **Frontend framework**는 “에이전트 앱의 UI를 만들기 위한 컴포넌트/라이브러리/도구 모음”이다.  
즉, 에이전트가 아무리 똑똑해도 **사용자가 입력하고 결과를 확인하는 인터페이스가 없으면 제품이 되기 힘듬.**
이게 왜 중요하냐면, Agentic AI는 “한 번 답하고 끝”이 아니라  
**대화 중간에 계획을 바꾸고, 도구를 호출하고, 중간 결과를 보여주고, 사용자 확인(HITL)을 받고, 다시 진행**하는 흐름이 많기 때문.


---
그렇다면, 사용되는 UI tool은 무엇인가.?

![Gradio](images2/gradio.png)
프로토타입/내부 데모용 UI는 보통 **Gradio, Mesop**처럼 “빨리 만들고 빨리 실험”하는 프레임워크를 쓴다. 
구현 속도가 빠르고, 백엔드도 단순하게 붙일 수 있어서 request–response 구조만으로도 충분한 경우가 많다. 
PoC, 연구 데모, 툴 연동 테스트에 특히 잘 맞는다.

![Streamlit](images2/stream.png)
반대로 외부 사용자에게 제공하는 **프로덕션 UI**는 **Streamlit, React, Flutter AI Toolkit**처럼 제
품 수준의 프레임워크가 더 적합하다. 이 경우 UI는 단순 입력/출력 창을 넘어서, **스트리밍 응답(토큰 단위 출력)**, 
진행 상태 표시, 커스텀 컴포넌트, stateless API 설계, 세션/메모리의 외부화 같은 요구사항이 자연스럽게 따라온다. 
즉, “UI 선택”이 곧 “백엔드 아키텍처 요구사항”을 결정한다.
---

## 2) AG-UI: Frontend와 Agent를 “실시간으로 연결”하는 통신 레이어

여기서 등장하는 개념이 **AG-UI(Agent–User Interaction protocol)**
Google Cloud 문서는 AG-UI를 통해 Frontend 프레임워크와 AI 에이전트 간 실시간 통신을 관리할 수 있다고 설명한다.  
AG-UI를 쉽게 풀면, 이런 기능을 위한 “약속(프로토콜)”이다.
- 에이전트의 응답을 **언제 렌더링할지**
- 앱의 **상태(state)를 언제 업데이트할지**
    - 필요한 경우 **클라이언트 측 액션을 언제 트리거할지**  
![AG-UI](images2/AG_UI.png)

## 3) Agent development framework: 에이전트 로직을 만드는 ‘뼈대’

자, 이제 사용자와 에이전트가 대화하는 창인 **AG-UI**를 봤으니,  
이번에는 에이전트의 **팔·다리(툴)**와 **기억(메모리)**을 설계하는 팔레트,  
즉 **Agent Development Framework**를 알아보자.

에이전트는 “무슨 일을 시키느냐”에 따라 구조가 달라진다.  
어떤 에이전트는 도구가 2~3개면 충분하지만, 어떤 에이전트는 검색·DB·브라우저·코드 실행까지 여러 도구가 필요하다.  
메모리도 마찬가지다. 단기 세션만으로 되는 경우도 있고, 사용자별 장기 기억이 꼭 필요한 경우도 있다.

그럼 이런 부품(툴/메모리/에이전트 루프)을 **빠르게 조립하고 운영**할 수 있는 ‘팔레트 공간’이 있을까?  
이미 수많은 프레임워크가 있고, 그중 Google이 오픈소스로 제공하는 선택지가 **ADK(Agent Development Kit)** 다.

![googe_adk_yotube](images2/adk_youtube.png)

**ADK(Agent Development Kit)** 를 쓰면, 에이전트의 기본 루프(상태 관리, 도구 호출, 멀티 에이전트 오케스트레이션 등)를 소프트웨어 개발처럼 구조화해서 빠르게 만들 수 있다.


![google_adk_github](images2/adk_github.png)

또 다른 선택지로는 **Langchain**이 있다.

![langchain_adk](images2/langchain.png)

Langchain은 에이전트 개발을 위한 오픈소스 프레임워크로, 다양한 도구와 라이브러리를 통합해서 에이전트 개발을 용이하게 해준다.

Langchain은 LLM, 메모리, 도구를 연결하는 **체인(chains)**과 복잡한 작업을 자동화하는 **에이전트(agent)** 추상화를 제공하며,
특정 목적에 맞춰 프롬프트 템플릿과 도구를 조합하는 워크플로우를 빠르게 구축할 수 있다.
또한 벡터 검색, 데이터베이스, 브라우저, 코드 실행기 등 외부 서비스를 연결할 수 있는 **커넥터**와,
대화 세션을 관리하는 **메모리 저장소**(예: `ConversationChain`, `ConversationBufferMemory`)를 쉽게 추가할 수 있어,
에이전트에게 과거 대화를 기억시키거나 사용자별 상태를 유지시키는 것도 간단하다.
(이후에 langchain 을 따로 post할 예정.)
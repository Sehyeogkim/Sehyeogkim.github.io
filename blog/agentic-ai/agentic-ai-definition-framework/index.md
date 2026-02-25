---
title: "🎐 Agentic AI - Definition & Framework"
layout: knowledge-home
source_url: "https://www.notion.so/3102a46dc68c8040b73cd27c851ca3e9"
source_id: "3102a46d-c68c-8040-b73c-d27c851ca3e9"
date: "2026-02-25T11:54:23.047Z"
category: "Agentic_AI"
---

Source: [https://www.notion.so/3102a46dc68c8040b73cd27c851ca3e9](https://www.notion.so/3102a46dc68c8040b73cd27c851ca3e9)


# Contents
- Agentic AI defnition - 기본 정의
- <span color="red">**Frontend framework: 사용자가 대화/작업을 요청하는 UI (part1)**</span>
- <span color="red">**Agent development framework: 에이전트 로직(루프, 상태, 도구 연결)을 만드는 프레임워크  (part1)**</span>
- **Agent tools: 검색, DB, 사내 API 등 “행동”을 수행하는 도구 묶음 (part1)**
- **\*\*Agent memory\*\*: 대화/세션 상태와 장기 기억 저장 (part1)**
- \*\*Agent design patterns\*\*: 싱글 에이전트 vs 멀티 에이전트 등 구조 패턴 (part3)
- \*\*Agent runtime\*\*: 에이전트 애플리케이션이 실제로 돌아가는 실행 환경 (part3)
- \*\*AI models\*\*: 추론/의사결정 엔진(part 3)
- \*\*Model runtime\*\*: 모델을 서빙하는 인프라(관리형 API/컨테이너/GKE 등) (part 3)

![🎐 Agentic AI - Definition & Framework](./images/img-001.png)




 
# Contents
- Large Language model
- 젠슨황의 연설 “perception → generative → agentic → physical
- AGI what is it? (at the end)
- Agentic AI structures (just simple will be dealted prciesly on next blog)
- Agentic Ai examples.

AI 라는 단어를 하루에 몇번을 듣는 건지, 새로운 기술들은 끊임 없이 나오고, 업데이트된 소식을 알지 못하면 뒤처지는 기분이 든다. (실제로 뒤쳐지는게 맞다).  일단 가장 중요한 LLM의 개념을 살펴보고 agentic ai를 이어서 살펴보자.

# What is LLM?
---
가장 빨리 발전하여 모든 인간에게 충격을 주었던, LLM(Large language model)은 아주 빠르게 발전을 하고 있고, 아래 사진의 여러 회사들이 경쟁중에 있다. 여기서 핵심은 response가 바로 자연어라는 점이다. 즉, 어떠한 ‘행동’을 하지 못하는 그냥 뇌와 같은 존재.
![🎐 Agentic AI - Definition & Framework](./images/img-002.png)
이 ‘뇌’가 실제로 일을 하도록, 검색을 하고, 파일을 읽고, 코드를 실행하고, 일정과 이메일을 다루고, 필요한 도구를 호출해 **환경과 상호작용**하게 만드는 시스템—바로 **Agentic AI(에이전틱 AI)** 이다.


#  젠슨 황 **CES 2025 기조연설(Keynote)**
---
![🎐 Agentic AI - Definition & Framework](./images/img-003.png)
젠슨 황이 제시한 큰 흐름은 “AI가 점점 더 **세상을 이해하고**, **콘텐츠를 만들고**, **일을 스스로 수행하고**, 마지막엔 **현실 세계에서 행동**하는 방향으로 진화한다”는 이야기입니다.
- **Perception AI**: 세상을 “읽는” 단계
- **Generative AI**: 읽은 정보를 바탕으로 “만드는” 단계
- **Agentic AI**: 도구를 써서 “일을 끝내는” 단계
- **Physical AI**: 현실에서 “움직이고 바꾸는” 단계
(현재 우리는 agentic AI 시대에 있음)
---
## 1) Perception AI: “세상을 보는 AI”
Perception AI는 카메라/마이크/라이다/센서 같은 입력을 받아서 **지금 상황이 무엇인지 인식**하는 AI 이며, 사람으로 치면 “눈과 귀” 역할.
Examples.
- 스마트폰 카메라가 “인물/음식/야경”을 자동 인식해 촬영 옵션을 바꿈
- 공장 카메라가 제품 결함(스크래치/누락)을 탐지
- 자율주행이 “차선/보행자/신호등”을 인식


---
## 2) Generative AI: “콘텐츠를 만드는 AI”
Generative AI는 우리가 가장 익숙한 형태의 AI이다. 바로 우리가 매일 쓰는 Chatgpt, gemini 즉 LLM이 바로 이 형태이기 때문이다. 즉, 입력(프롬프트)을 받아서 **텍스트/이미지/코드** 같은 결과물을 “생성”합니다.
(하지만, 출력은 자연어/이미지 일 뿐, 스스로 무언가를 실행해서 일을 끝내지는 못한다.!!
### Examples.
- “이 논문 핵심만 요약해줘”
- “이메일을 더 공손하게 써줘”
- “이 코드 에러 고쳐줘”
- “이런 느낌의 썸네일 이미지 만들어줘”
---
## 3) Agentic AI: “일을 끝내는 AI”
우리가 현존하는 시대에자, 이 블로그 branch의 주제인, Agentic AI는 Generative AI(LLM)가 “말만 하는 뇌”에 머무르지 않고, **도구를 사용해 목표를 달성하도록 만든 시스템 그 자체이다. **LLM(뇌)에 \*\*손발(툴)\*\*을 달아준 형태라고 보면 이해가 빠릅니다.
### 쉬운 예시 1: “블로그 글 작성 에이전트”
- 목표: “Agentic AI 글 초안 작성 + 참고 자료 정리”
- 행동 흐름:
	1. 최신 자료 검색 → 2) 핵심 문장/근거 수집
	2. 목차 구성 → 4) 초안 작성 → 5) 출처 정리
### 쉬운 예시 2: “업무 에이전트”
- 목표: “회의록 정리하고 팀에 공유”
- 행동 흐름:
	1. 회의 노트 읽기 → 2) 결정사항/To-do 추출
	2. 담당자 할당 → 4) 노션/슬랙에 업로드 → 5) 일정 등록
---
## 4) Physical AI: “현실에서 움직이는 AI”
![🎐 Agentic AI - Definition & Framework](./images/img-004.png)

그 다음 단계인, Physical AI는 로봇, 자율주행, 드론처럼 **물리 세계에서 실제로 행동**하는 AI. Agentic AI가 디지털 도구(API, 브라우저, 파일)를 다룬다면, Physical AI는 **모터/로봇 팔/차량 제어**로 현실에 영향을 준다. 아직 이 단계를 완벽히 구현하지 못하는 이유는, 물리 세계에서의 행동은 난이도가 훨씬 높습니다.
1. **실패 비용이 큼**: 사람 안전, 물건 파손, 사고 위험
2. **변수가 많음**: 마찰/무게/가림/센서 노이즈 등 현실은 예측이 어려움
3. **실시간성**: 즉각적인 판단과 제어가 필요

종합적으로 요약을 한다면,
---
- **Perception AI**는 세상을 “읽고”,
- **Generative AI**는 결과물을 “만들고”,
- **Agentic AI**는 도구로 일을 “끝내고”,
- **Physical AI**는 현실에서 “움직여서 바꾼다”.

# Last stage. AGI
---
![🎐 Agentic AI - Definition & Framework](./images/img-005.png)
- **Artificial General Intelligence**: 사람처럼 **다양한 영역에서 새로운 문제를 스스로 학습하고 해결**할 수 있는 “범용 지능”을 뜻합니다. 즉, 지금까지는 문제 자체를 user가 정의해서 넘겨주었다면, 이제 문제를 발견 하고 해결하는 모든 과정을 aI가 주도적으로 하는 단계이다.
- 핵심은 단순 생성이 아니라:
	- 폭넓은 일반화(새로운 도메인 적응)
	- 장기 계획과 목표 유지
	- 현실 세계에서의 안정적 추론/학습
	- 스스로 능력을 확장하는 문제 해결

# Structure of Agentic AI
---

![🎐 Agentic AI - Definition & Framework](./images/img-006.png)
구글에서 제공하는 agentic ai의 설계구조도면은 위와 같다. user아 agent에게 어떠한 요청을 하게 되면, agent는 자신이 가지고 있는 Tools, memory를 바탕으로 그 문제를 해결하고, 해결하는 사고 과정으로 (AI model, LLM)을 사용한다.

# examples
---
마지막으로 한가지 예시를 들면서 전체적으로 agentic ai가 어떠한 흐름으로 흐르는 지를 살펴보자
![🎐 Agentic AI - Definition & Framework](./images/img-007.png)
![🎐 Agentic AI - Definition & Framework](./images/img-008.png)
LinkedIn의 **Hiring Assistant**는 채용 담당자(recruiter)의 업무를 자동화하고 보조하기 위해 설계된 **에이전트형 AI(Agentic AI)** 입니다. 단순히 질문에 답하는 챗봇이 아니라, 채용 프로세스에서 반복적으로 발생하는 작업들을 실제로 “처리”해주는 쪽에 가깝습니다.
예를 들어 Hiring Assistant는 다음과 같은 업무를 도와줍니다.
- 지원자에게 보낼 **아웃리치(outreach) 메시지 초안 작성**
- 직무에 맞는 **스크리닝 질문 생성**
- LinkedIn이 보유한 방대한 채용 데이터(프로필/이력/네트워크 등)를 기반으로 **후보자 소싱(sourcing)**
즉, LinkedIn의 채용 생태계 데이터를 활용해, 채용 담당자가 “해야 할 일”을 더 빠르게 끝낼 수 있도록 워크플로우를 지원합니다.
또 흥미로운 점은 Hiring Assistant가 **모듈형 멀티 에이전트 시스템**으로 설계되어 있다는 점입니다. 구조적으로는 한 명의 **총괄 에이전트(감독/오케스트레이터, supervisory agent)** 가 여러 개의 **서브 에이전트(sub-agents)** 를 지휘하는 형태입니다. 각 서브 에이전트는 채용 업무 중 하나의 기능을 담당합니다.
- 채용 공고(Job description) 초안 작성 에이전트
- 후보자 소싱 에이전트
- 메시지 작성 에이전트
- 후보자 평가/랭킹 에이전트
- (기타 필요한 세부 기능별 에이전트)
채용 담당자가 “이 포지션에 맞는 후보자 찾아서 첫 메시지까지 작성해줘” 같은 요청을 하면, 총괄 에이전트가 이를 더 작은 작업 단위로 쪼갭니다. 그리고 각 작업에 맞는 서브 에이전트를 호출해 결과를 받아오고, 결과들을 종합·정리해서 채용 담당자에게 최종 출력으로 제공합니다.
마지막으로, Hiring Assistant는 모든 사용자가 하나의 에이전트를 공유하는 방식이 아니라, **채용 담당자(리크루터)마다 별도의 에이전트 인스턴스**가 붙는 구조로 설명됩니다. 즉, 각 리크루터의 맥락(채용 포지션, 선호, 진행 중인 파이프라인 등)에 맞게 더 개인화된 작업 수행이 가능하도록 설계된 것입니다.

여기까지 agentic ai가 무엇인지에 대해서 알아보았고, structure of it을 더 자세하게 다음 쳅터에서 파보도록 하자.

# Fronted Framework
---
Google Cloud 문서에서 정의한 \*\*Frontend framework\*\*는 “에이전트 앱의 UI를 만들기 위한 컴포넌트/라이브러리/도구 모음”이다.   즉, 에이전트가 아무리 똑똑해도 \*\*사용자가 입력하고 결과를 확인하는 인터페이스가 없으면 제품이 되기 힘듬.\*\* 이게 왜 중요하냐면, Agentic AI는 “한 번 답하고 끝”이 아니라, \*\*대화 중간에 계획을 바꾸고, 도구를 호출하고,중간 결과를 보여주고, 사용자 확인(HITL)을 받고, 다시 진행\*\*하는 흐름이 많기 때문이다.


### UI - tools
---
![🎐 Agentic AI - Definition & Framework](./images/img-009.png)
agent와의 대화와 실행되는 action의 결과를 사용자가 실시간으로 빠르게 확인할 수 있어야 한다.<br>따라서, 프로토타입/내부 데모용 UI는 보통 \*\*Gradio, Mesop\*\*처럼 “빨리 만들고 빨리 실험”하는 프레임워크를 쓴다. 구현 속도가 빠르고, 백엔드도 단순하게 붙일 수 있어서 request–response 구조만으로도 충분한 경우가 많다. PoC, 연구 데모, 툴 연동 테스트에 특히 잘 맞는다.

![🎐 Agentic AI - Definition & Framework](./images/img-010.png)
<br>반대로 외부 사용자에게 제공하는 \*\*프로덕션 UI\*\*는 \*\*Streamlit, React, Flutter AI Toolkit\*\*처럼 제품 수준의 프레임워크가 더 적합하다. 이 경우 UI는 단순 입력/출력 창을 넘어서, \*\*스트리밍 응답(토큰 단위 출력)\*\*, 진행 상태 표시, 커스텀 컴포넌트, stateless API 설계, 세션/메모리의 외부화 같은 요구사항이 자연스럽게 따라온다. 즉, “UI 선택”이 곧 “백엔드 아키텍처 요구사항”을 결정한다.


# AG UI
---
![🎐 Agentic AI - Definition & Framework](./images/img-011.png)
여기서 등장하는 개념이 바로 \*\*AG-UI(Agent–User Interaction protocol)\*\*.<br>Google Cloud 문서에 따르면, AG-UI를 통해 Frontend 프레임워크와 AI 에이전트 간 실시간 통신을 관리할 수 있다고 설명한다.AG-UI를 쉽게 풀면, 이런 기능을 위한 “약속(프로토콜)”이다. (이후에 설명되는 MCP와 비슷한 개념)<br>- 에이전트의 응답을 \*\*언제 렌더링할지\*\*<br>- 앱의 \*\*상태(state)를 언제 업데이트할지\*\*<br>- 필요한 경우 \*\*클라이언트 측 액션을 언제 트리거할지\*\*<br>를 약속하는 것이다.<br><br><br>

# Agent Development Framework.
---
![🎐 Agentic AI - Definition & Framework](./images/img-012.png)
google cloud ADK youtube channel: [https://www.youtube.com/watch?v=pX0_iIfRilU](<https://www.youtube.com/watch?v=pX0_iIfRilU>)<br>
그렇다면, 우리는 도대체 어디서 agent ai를 설계해야할까? LLM(뇌)와 사용자를 연결하는 AG-UI에 대해서 알아보았고,이후에 다룰 팔 다리인 tools, skills and so on을 연결하고 해체하고 편집하는 공간이 있어야한다. 그 공간 이자 작업자의 팔레트가 바로 \*\*Agent Development Framework\*\*이다.<br><br>에이전트는 “무슨 일을 시키느냐”에 따라 구조가 달라진다.<br>어떤 에이전트는 도구가 2\~3개면 충분하지만, 어떤 에이전트는 검색·DB·브라우저·코드 실행까지 여러 도구가 필요하다.  메모리도 마찬가지다. 단기 세션만으로 되는 경우도 있고, 사용자별 장기 기억이 꼭 필요한 경우도 있다.<br>(즉, 사용자의 목적에 맞는 agent를 build할 수 있게 된다.)<br><br>이미 수많은 회사들이 자신이 build한 프레임 워크를 공개하고 있고, 그중 Google이 오픈소스로 제공하는 선택지가 \*\*ADK(Agent Development Kit)\*\* 다. (이후 application 단계에서 자세하게 살펴보도록 하자)
![🎐 Agentic AI - Definition & Framework](./images/img-013.png)




ADK를 제공하는 또 다른 플랫폼 기업인 (굉장히 빠르게 성장중에 있음)
### Langchain
---
![🎐 Agentic AI - Definition & Framework](./images/img-014.png)

Langchain은 LLM, 메모리, 도구를 연결하는 \*\*체인(chains)\*\*과 복잡한 작업을 자동화하는 \*\*에이전트(agent)\*\* 추상화를 제공하며, 특정 목적에 맞춰 프롬프트 템플릿과 도구를 조합하는 워크플로우를 빠르게 구축할 수 있다. 또한 벡터 검색, 데이터베이스, 브라우저, 코드 실행기 등 외부 서비스를 연결할 수 있는 \*\*커넥터\*\*와,<br>대화 세션을 관리하는 \*\*메모리 저장소\*\*(예: \`ConversationChain\`, \`ConversationBufferMemory\`)를 쉽게 추가할 수 있어, 에이전트에게 과거 대화를 기억시키거나 사용자별 상태를 유지시키는 것도 간단하다.<br>(이후에 langchain 을 따로 post할 예정.)

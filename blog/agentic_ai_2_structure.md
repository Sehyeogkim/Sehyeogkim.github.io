---
title: "Agentic AI 구조 완전 정복: Planning과 Tools를 중심으로"
date: 2026-02-23
tags: [AgenticAI, AI-Agent, Architecture, GoogleCloud, Planning, Tools]
---

# Agentic AI 구조 완전 정복: Planning과 Tools를 중심으로

Agentic AI를 한 문장으로 정리하면, **사용자 의도를 이해하고 → 여러 단계 계획을 세우고 → 도구를 호출해 실행까지 끝내는** 자율 시스템입니다. 단순히 “답변을 생성하는 모델”이 아니라, **계획(Planning)** 과 **도구(Tools)** 를 통해 실제 업무를 완료하도록 설계된 아키텍처라고 보면 됩니다. :contentReference[oaicite:1]{index=1}

이 글에서는 Google Cloud의 가이드 문서를 기반으로, Agentic AI 시스템을 구성할 때 어떤 컴포넌트가 필요하고, 그중에서도 핵심인 **Planning**과 **Tools**를 어떻게 설계하면 좋은지 쉽게 정리해보겠습니다. :contentReference[oaicite:2]{index=2}

---

## 0. Agentic AI 아키텍처를 구성하는 큰 블록들

Google Cloud 문서는 에이전트 시스템을 크게 다음 컴포넌트들로 정리합니다. :contentReference[oaicite:3]{index=3}

- **Frontend framework**: 사용자가 대화/작업을 요청하는 UI
- **Agent development framework**: 에이전트 로직(루프, 상태, 도구 연결)을 만드는 프레임워크
- **Agent tools**: 검색, DB, 사내 API 등 “행동”을 수행하는 도구 묶음
- **Agent memory**: 대화/세션 상태와 장기 기억 저장
- **Agent design patterns**: 싱글 에이전트 vs 멀티 에이전트 등 구조 패턴
- **Agent runtime**: 에이전트 애플리케이션이 실제로 돌아가는 실행 환경
- **AI models**: 추론/의사결정 엔진(LLM 등)
- **Model runtime**: 모델을 서빙하는 인프라(관리형 API/컨테이너/GKE 등)

여기서 오늘의 주제는 이 중에서도 “에이전트를 에이전트답게 만드는” 두 축:

> **Planning(계획)** = “무엇을 어떤 순서로 할지 결정하는 능력”  
> **Tools(도구)** = “결정한 일을 실제로 실행하는 손발”

입니다.

---

# 1. Planning: 에이전트가 ‘스스로 일하는’ 느낌이 나는 이유

Agentic AI의 목표는 “사용자 의도를 이해하고, **멀티스텝 계획**을 만들고, 그 계획을 도구로 실행하는 것”입니다. 즉 Planning은 옵션이 아니라 **핵심 능력**입니다. :contentReference[oaicite:4]{index=4}

## 1.1 Planning은 무엇을 포함하나?

에이전트의 Planning을 현실적으로 풀어쓰면 보통 다음을 포함합니다.

- **요구사항 분해**: 큰 요청을 작은 작업으로 쪼개기  
  예) “채용 공고 올리고 후보자 찾아서 메시지 보내줘” → JD 작성 / 후보 소싱 / 메시지 작성 / 후보 랭킹
- **도구 선택**: 지금 단계에서 어떤 도구가 최적인지 고르기  
- **검증 및 재시도**: 결과가 불충분하거나 실패하면 경로를 바꿔 재시도

이 과정이 잘 되면 사용자는 “그냥 대답만 하는 AI”가 아니라 “일을 처리하는 비서/에이전트”라고 느끼게 됩니다.

---

## 1.2 모델 자체의 추론 능력이 Planning 품질을 좌우한다

Google Cloud 문서에서는 에이전트 성능을 높이려면 **모델의 추론(reasoning) 능력**을 조절할 수 있다고 설명합니다. 예를 들어 최신 Gemini 모델에는 멀티스텝 계획에 도움이 되는 “thinking process”가 있고, 디버깅을 위해 thought summaries(사고 요약)를 참고할 수 있다고 합니다. :contentReference[oaicite:5]{index=5}

### 핵심 개념: thinking budget
또한 **thinking budget(생각 토큰 예산)** 을 조정해, 작업 복잡도가 높을수록 더 깊은 계획/추론을 하게 만들 수 있습니다. 다만 thinking budget을 올리면 품질이 좋아질 수 있지만, **지연(latency)과 비용(cost)** 이 증가할 수 있다는 trade-off도 명확히 언급합니다. :contentReference[oaicite:6]{index=6}

> 정리:  
> **계획 품질** ↔ **비용/지연** 사이의 균형을 설계로 잡아야 합니다.

---

## 1.3 Model routing: “작은 일은 가볍게, 어려운 일만 비싸게”

문서에서는 성능과 비용 최적화를 위해 **model routing**을 추천합니다. 쉬운 작업은 더 작은 모델(SLM)로 처리하고, 복잡한 추론이 필요한 작업에만 더 강력한 모델을 쓰는 식입니다. :contentReference[oaicite:7]{index=7}

예를 들어:

- **SLM/가벼운 모델**: 형식이 정해진 텍스트 분류, 간단한 코드 생성, 단순 질의
- **대형 모델**: 복잡한 의사결정, 멀티스텝 계획, 예외 처리 많은 업무

이런 라우팅을 잘하면 “항상 최고 성능 모델로 밀어붙이는 설계”보다 훨씬 현실적인 운영이 가능합니다. :contentReference[oaicite:8]{index=8}

---

# 2. Tools: 에이전트의 ‘손발’—어떤 방식으로 붙일 것인가

도구가 없으면 에이전트는 결국 “말만 잘하는 존재”로 머뭅니다. 도구는 에이전트가 외부 데이터/시스템을 호출하고 실제 행동을 하게 만드는 핵심 레이어입니다. :contentReference[oaicite:9]{index=9}

Google Cloud 문서는 도구 선택을 사용 사례별로 크게 네 가지로 정리합니다. :contentReference[oaicite:10]{index=10}

## 2.1 Built-in tools: 빠르게 시작하고 싶을 때

ADK(Agent Development Kit)에는 런타임에 바로 통합되는 built-in tools가 있고, 외부 통신 프로토콜 설정 없이 함수처럼 호출할 수 있다고 설명합니다. :contentReference[oaicite:11]{index=11}

또 이 built-in tools는 예를 들어:
- 웹에서 실시간 정보 접근
- 안전한 환경에서 코드 실행
- 사내 데이터 기반 RAG를 위한 프라이빗 데이터 접근
- 클라우드 DB 같은 정형 데이터 상호작용

같은 “자주 필요한 공통 기능”을 제공한다고 합니다. :contentReference[oaicite:12]{index=12}

**언제 좋나?**
- 프로토타입, PoC
- 도구 연결을 빨리 하고 에이전트 로직에 집중하고 싶을 때

---

## 2.2 MCP(Model Context Protocol): 모듈형/멀티 에이전트로 가려면

멀티 에이전트나 모듈형 시스템에서는 “도구가 늘어나고, 다른 에이전트도 같은 도구를 쓰고, 교체 가능해야” 합니다. 이때 문서는 **MCP**를 “표준화된 인터페이스”로 소개합니다. :contentReference[oaicite:13]{index=13}

문서의 비유가 아주 직관적인데, MCP는 하드웨어 포트처럼 **에이전트의 추론 로직과 도구 구현을 분리(decouple)** 해주어, 도구 통합을 단순화하고 상호운용성을 높인다고 설명합니다. :contentReference[oaicite:14]{index=14}

**언제 좋나?**
- 도구를 재사용/공유하고 싶을 때
- 멀티 에이전트에서 동일한 툴 체계를 갖추고 싶을 때
- 도구가 자주 바뀌거나 확장되는 조직

---

## 2.3 API management platform: 엔터프라이즈 규모의 “도구 운영”

도구가 많아지면 “연동”보다 더 큰 문제가 생깁니다:  
**보안, 인증, 모니터링, 장애 대응, 정책 관리** 같은 운영 이슈죠.

문서는 “대규모 API 기반 도구를 엔터프라이즈 스케일로 관리/보안/모니터링해야 한다면 API 관리 플랫폼”을 고려하라고 정리합니다. :contentReference[oaicite:15]{index=15}

**언제 좋나?**
- 도구가 조직 내부 API/외부 SaaS로 매우 많을 때
- 권한, 레이트 리밋, 감사 로그가 중요한 환경

---

## 2.4 Custom function tools: MCP 서버가 없거나 특수 API일 때

MCP 서버가 없거나 특정 사내/서드파티 API를 꼭 붙여야 한다면, custom function tools로 통합하는 케이스를 제시합니다. :contentReference[oaicite:16]{index=16}

---

## 2.5 “좋은 도구”의 조건: 관측 가능성(Observability) + 에러 핸들링

문서는 도구를 고를 때 기능만 보지 말고, **운영 신뢰성**을 같이 평가하라고 강조합니다. 특히:

- **observable(관측 가능)** 해야 디버깅/추적이 쉽고
- **에러 핸들링**이 탄탄해야 실패를 빠르게 복구할 수 있으며
- 결과적으로 “어떤 액션이 왜 실패했는지 trace”할 수 있어야 한다고 말합니다. :contentReference[oaicite:17]{index=17}

이 포인트는 실제 서비스에서 정말 중요합니다. Agentic AI는 “한 번의 답변”이 아니라 “연속된 행동”이라서, 한 단계만 실패해도 전체가 무너질 수 있기 때문입니다.

---

# 3. (짧게) Memory와 Pattern: Planning/Tools와 붙어 있는 필수 요소

오늘 포커스는 Planning과 Tools이지만, 둘이 잘 돌아가려면 Memory와 Pattern도 함께 이해해야 합니다.

## 3.1 Memory: 세션 상태(단기)와 장기 기억(장기)

문서는 에이전트가 “일관된 경험”을 주려면 short-term memory와 long-term memory가 필요하다고 설명합니다. :contentReference[oaicite:18]{index=18}

- **Short-term memory**: 한 대화 세션 안에서의 컨텍스트 유지(세션/상태)  
- **Long-term memory**: 사용자별로 대화를 넘어 지속되는 지식 베이스

특히 운영 환경에서는 인메모리로만 두지 말고, stateless 앱 + 외부 저장소로 상태를 관리하는 방식이 수평 확장에 유리하다고 안내합니다(예: Redis/Firestore/Agent Engine sessions 등). :contentReference[oaicite:19]{index=19}

## 3.2 Pattern: 싱글 에이전트부터 시작하고, 필요할 때 멀티로

문서는 **싱글 에이전트**를 “좋은 출발점”으로 추천합니다. 프롬프트/도구 정의/핵심 루프를 먼저 다듬고, 복잡도가 커질 때 **멀티 에이전트**로 확장하라는 흐름입니다. :contentReference[oaicite:20]{index=20}

---

# 4. 마무리: Agentic AI는 “계획 + 도구 + 운영”의 문제다

정리하면, Agentic AI를 잘 만든다는 건 단순히 LLM을 붙이는 게 아니라:

- **Planning 품질**을 올리기 위한 모델 선택/추론 예산/라우팅 설계 :contentReference[oaicite:21]{index=21}
- **Tools 통합**을 빠르게/안전하게/확장 가능하게 설계(Built-in → MCP → API mgmt) :contentReference[oaicite:22]{index=22}
- 그리고 도구가 늘어날수록 더 중요해지는 **관측 가능성(Observability)과 오류 대응**을 갖추는 것 :contentReference[oaicite:23]{index=23}

이 세 가지를 시스템 차원에서 풀어내는 과정입니다.

---

## 다음 글 예고
다음 글에서는 이 구조를 더 “실전”으로 가져가서,
- Planning을 구현하는 대표 루프(Plan → Act → Check → Retry)
- Tool 실패 시 fallback 전략(대체 도구/재시도/부분 완료)
- 멀티 에이전트 오케스트레이션(슈퍼바이저-서브에이전트 패턴)

을 예시 중심으로 정리해보겠습니다.
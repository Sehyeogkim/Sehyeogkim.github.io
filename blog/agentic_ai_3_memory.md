---
layout: post
title: "Agentic AI 구조 part2 - memory"
date: 2026-02-23
author: Jeff
categories: [theory, agentic-ai]
---



다시, Agentic AI를 한 문장으로 정리하면, **사용자 의도를 이해하고 → 여러 단계 계획을 세우고 → 도구를 호출해 실행까지 끝내는** 자율 시스템이다.
단순히 “답변을 생성하는 모델”이 아니라, **계획(Planning)** 과 **도구(Tools)** 를 통해 실제 업무를 완료하도록 설계된 아키텍처인 것.

---

## 0. Agentic AI 아키텍처를 구성하는 큰 블록들

Google Cloud 문서에서 정의한, 에이전트 시스템 요소들.

- Frontend framework: 사용자가 대화/작업을 요청하는 UI
- Agent development framework: 에이전트 로직(루프, 상태, 도구 연결)을 만드는 프레임워크
- **Agent tools**: 검색, DB, 사내 API 등 “행동”을 수행하는 도구 묶음
- **Agent memory**: 대화/세션 상태와 장기 기억 저장
- Agent design patterns: 싱글 에이전트 vs 멀티 에이전트 등 구조 패턴
- Agent runtime: 에이전트 애플리케이션이 실제로 돌아가는 실행 환경
- AI models: 추론/의사결정 엔진(LLM 등)
- Model runtime: 모델을 서빙하는 인프라(관리형 API/컨테이너/GKE 등)

여기서 오늘의 주제는 이 중에서도 tools와 memory에 대해서 이야기 해보자.

![Agentic AI 아키텍처](images2/agentic_ai_structure.svg)



## tools


## memory

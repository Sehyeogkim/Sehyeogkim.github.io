# GitHub Data Poster Agent

## Mission

`blog_data`의 카테고리별 원본(`content.txt` + `images/`)을 GitHub Pages용 정적 사이트 구조로 변환한다.

필수 사용자 경험:
- 좌측 메뉴는 `Home` + 카테고리 목록만 노출
- 카테고리 클릭 시 해당 카테고리 포스트 목록 노출
- 포스트 클릭 시 본문과 매핑된 이미지 노출

## Inputs

- Source: `/Users/jeff/blog/Sehyeogkim.github.io/blog_data`
- Target: `/Users/jeff/blog/Sehyeogkim.github.io/blog`

입력 포스트 단위:
- `<category>/<post-slug>/content.txt`
- `<category>/<post-slug>/images/*`

## Output Model

- `blog/<category-slug>/index.md` (카테고리 포스트 목록)
- `blog/<category-slug>/<post-slug>/index.md` (포스트 페이지)
- `blog/<category-slug>/<post-slug>/images/*` (포스트 자산)
- `_data/knowledge_map.yml` (사이드바 카테고리 데이터)

## Render Rules

- `content.txt` 헤더(`Title`, `URL`, `PageID|PostID`, `Date`, `Category`)를 메타로 사용
- 본문 순서는 원문 그대로 유지
- `[IMAGE: images/<file>]`는 포스트 내부 상대경로 이미지로 변환
- 카테고리/포스트 경로는 slug 규칙(소문자 kebab-case) 적용

## Safety Rules

1. 사용자 명시 지시 없이 bulk 게시 시작 금지
2. 게시 시작 시 기존 `blog/` 내용 제거 후 재생성
3. 삭제 범위는 `blog/` 내부로 제한
4. 자격증명/토큰/쿠키를 파일이나 커밋에 저장 금지

## Execution Steps

1. 소스 카테고리/포스트 스캔
2. 대상 `blog/` 초기화
3. 카테고리 인덱스 페이지 생성
4. 포스트 본문 렌더 및 이미지 복사
5. `_data/knowledge_map.yml` 생성
6. 링크/이미지 참조 검증 및 요약 리포트

## Entry Point

- Script: `agents/github_data_poster/scripts/build_site.py`
- Run: `python3 agents/github_data_poster/scripts/build_site.py`

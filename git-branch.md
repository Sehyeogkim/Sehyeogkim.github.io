# Git Branch 완전 가이드

## Git Branch 개념 이해하기

### Branch란 무엇인가?

**Branch = 독립적인 개발 라인**

💡 **중요**: Branch는 파일 시스템의 폴더/디렉토리와 **완전히 다릅니다**!

#### Branch의 특징:
- 같은 프로젝트에서 **여러 버전**을 동시에 개발할 수 있음
- 각 branch는 독립적으로 커밋할 수 있음
- 나중에 branch들을 합칠 수 있음 (merge)

#### Branch 예시:
```
프로젝트: 쇼핑몰 웹사이트

main 브랜치 (메인 개발)
├── 기능 A 개발 완료
├── 기능 B 개발 중
└── 버그 수정

feature/login 브랜치 (로그인 기능 개발용)
├── 로그인 폼 UI
├── 로그인 API 연동
└── 회원가입 기능

hotfix/payment 브랜치 (결제 버그 긴급 수정용)
└── 결제 오류 수정
```

### Branch 사용 이유:
1. **안전한 개발**: 메인 코드를 망가뜨리지 않고 새 기능 개발
2. **협업**: 여러 사람이 동시에 다른 기능 작업
3. **실험**: 새로운 아이디어 테스트
4. **버전 관리**: 버그 수정과 신규 개발 분리

## 🚀 새로운 Branch 만들기 - 완전 가이드

### 방법 1: 새 브랜치 만들기 (가장 간단한 방법)
```bash
git checkout -b 새브랜치이름
```
**한 번에 두 가지 작업:**
1. 새 브랜치 생성
2. 그 브랜치로 자동 이동

**예시:**
```bash
git checkout -b feature/user-login
git checkout -b bugfix/header-layout
git checkout -b hotfix/payment-error
```

### 방법 2: 두 단계로 만들기
```bash
# 1단계: 브랜치 생성 (현재 브랜치에 머무름)
git branch 새브랜치이름

# 2단계: 새 브랜치로 이동
git checkout 새브랜치이름
```

### 방법 3: 특정 커밋에서 브랜치 만들기
```bash
# 특정 커밋 해시에서 브랜치 만들기
git branch 새브랜치이름 커밋해시

# 예시: 이전 버전에서 브랜치 만들기
git branch hotfix/old-bug abc1234
```

### Branch 이름 짓기 규칙 (Best Practices)

#### 기능 개발 브랜치
```bash
git checkout -b feature/기능이름
# 예시:
git checkout -b feature/user-authentication
git checkout -b feature/shopping-cart
git checkout -b feature/payment-integration
```

#### 버그 수정 브랜치
```bash
git checkout -b bugfix/버그설명
# 예시:
git checkout -b bugfix/login-validation
git checkout -b bugfix/mobile-responsive
```

#### 긴급 수정 브랜치
```bash
git checkout -b hotfix/문제설명
# 예시:
git checkout -b hotfix/server-crash
git checkout -b hotfix/security-patch
```

#### 실험/테스트 브랜치
```bash
git checkout -b experiment/아이디어
# 예시:
git checkout -b experiment/new-ui-design
git checkout -b experiment/dark-mode
```

### 새로운 브랜치 만들기 전 체크사항

#### 1. 현재 상태 확인
```bash
git status              # 작업 중인 파일들 확인
git branch              # 현재 브랜치 위치 확인
git log --oneline -3    # 최근 커밋들 확인
```

#### 2. main 브랜치 최신화 (권장)
```bash
git checkout main       # main 브랜치로 이동
git pull origin main    # 최신 코드 가져오기
```

#### 3. 새 브랜치 생성
```bash
git checkout -b feature/my-new-feature
```

### 실전 예시: 로그인 기능 개발

```bash
# 1. main 브랜치에서 시작
git checkout main
git pull origin main

# 2. 새 기능 브랜치 만들기
git checkout -b feature/login-system

# 3. 개발 작업 시작
# (파일 수정, 추가 등)
git add .
git commit -m "Add login form UI"

# 4. 계속 개발
git commit -m "Add form validation"
git commit -m "Connect to authentication API"

# 5. 작업 완료 후 main으로 돌아가기
git checkout main

# 6. 최신 코드 다시 가져오기
git pull origin main

# 7. 기능 브랜치 합치기
git merge feature/login-system

# 8. 사용 완료된 브랜치 삭제
git branch -d feature/login-system
```

### Branch 명령어들:

#### 기본 명령어
```bash
git branch              # 모든 브랜치 목록 보기
git branch 브랜치이름    # 새 브랜치 생성
git checkout 브랜치이름  # 브랜치로 이동
git checkout -b 새브랜치 # 새 브랜치 생성 + 이동
```

#### 브랜치 관리
```bash
git merge 브랜치명      # 다른 브랜치를 현재 브랜치로 합치기
git branch -d 브랜치명   # 브랜치 삭제
git branch -m 새이름     # 브랜치 이름 변경
```

#### 실무에서 자주 쓰는 패턴:
```bash
# 1. 새 기능 개발용 브랜치 만들기
git checkout -b feature/new-login

# 2. 기능 개발 (여러 번 커밋)
git add .
git commit -m "Add login form"
git commit -m "Add validation"

# 3. 메인 브랜치로 돌아가기
git checkout main

# 4. 최신 코드 가져오기
git pull origin main

# 5. 기능 브랜치 합치기
git merge feature/new-login

# 6. 합친 브랜치 삭제
git branch -d feature/new-login
```

### Branch 이름 짓기 관례:
- `main` 또는 `master`: 메인 브랜치
- `feature/기능이름`: 새 기능 개발
- `bugfix/버그이름`: 버그 수정
- `hotfix/긴급수정`: 긴급 수정
- `release/v1.2`: 버전 릴리즈

### 주의사항:
- **항상 main 브랜치를 깨끗하게 유지**하세요
- **작은 단위로 커밋**하세요
- **브랜치를 자주 push**해서 백업하세요

### 실습: Branch 사용해보기
지금 우리는 `feature/add-more-examples` 브랜치에 있어요!
이 브랜치에서 새로운 브랜치 관리 예제를 추가해볼게요.
# 자주 사용하는 Git 명령어 정리

## 기본 개념
Git은 **버전 관리 시스템**으로, 파일의 변경사항을 추적하고 협업을 쉽게 해줍니다.

### Git의 세 단계
1. **Working Directory**: 실제 작업하는 파일들
2. **Staging Area**: 다음 커밋에 포함될 변경사항들 (`git add`)
3. **Repository**: 커밋된 버전들 (`git commit`)

## 자주 사용하는 명령어들

### 1. `git status`
**현재 상태 확인**
```bash
git status
```
- 작업 디렉토리의 상태를 보여줍니다
- 어떤 파일이 수정되었는지, staging area에 있는지 확인
- **언제 쓰나?** 작업하기 전/후에 항상 확인하는 습관!

### 2. `git add`
**변경사항을 staging area에 추가**
```bash
git add 파일명        # 특정 파일만
git add .            # 모든 변경사항
git add *.txt        # 패턴으로 추가
```

**중요**: `git add .`는 **수정 후** 사용합니다!
- 수정한 파일들을 다음 커밋에 포함시키기 위해 staging area로 옮깁니다

### 3. `git commit`
**staging area의 변경사항을 저장**
```bash
git commit -m "커밋 메시지"
```

**커밋 메시지 작성 팁**:
- 현재형으로 작성: "Add login feature" (추가함)
- 명확하고 간결하게: "Fix bug in user registration"

### 4. `git push`
**로컬 커밋들을 원격 저장소로 업로드**
```bash
git push origin main
```

### 5. `git pull`
**원격 저장소의 최신 변경사항을 가져오기**
```bash
git pull origin main
```

### 6. `git log`
**커밋 히스토리 확인**
```bash
git log --oneline    # 간단히 보기
git log -5          # 최근 5개만
```

### 7. `git diff`
**변경사항 비교**
```bash
git diff            # working directory vs staging area
git diff --staged   # staging area vs 마지막 커밋
```

## 자주 하는 작업 흐름

### 새로운 작업 시작하기
```bash
git status           # 상태 확인
# 파일 수정/생성
git add .            # 변경사항 staging
git commit -m "설명"  # 커밋
git push             # 업로드
```

### 최신 코드 가져오기
```bash
git pull             # 원격 변경사항 가져오기
git status           # 충돌 확인
```

### 실수 복구
```bash
git checkout 파일명     # 파일 변경사항 취소
git reset HEAD 파일명   # staging 취소
```

## 팁
- `git status`를 자주 확인하세요!
- 커밋 메시지는 명확하게 작성하세요
- `git add .` 전에 `git status`로 어떤 파일들이 변경되었는지 확인하세요
- push 전에 pull로 최신 상태인지 확인하세요

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
지금 우리는 `feature/git-tutorial` 브랜치에 있어요!
이 브랜치에서만 존재하는 변경사항을 만들어볼게요.

## GitHub 관련 추가 명령어
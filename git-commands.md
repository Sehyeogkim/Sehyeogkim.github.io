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

## Git Branch & GitHub 관련 명령어

> 📖 **참고**: 자세한 Branch 사용법은 `git-branch.md` 파일을 확인하세요!

### Branch 기본 명령어
```bash
git branch              # 브랜치 목록 보기
git checkout -b feature/새기능  # 새 브랜치 만들기
git merge 브랜치명      # 브랜치 합치기
git branch -d 브랜치명   # 브랜치 삭제
```

## GitHub 관련 추가 명령어
# Git
## Git의 개념
- 분산 버전 관리 시스템
- 컴퓨터 파일의 변경 사항 추적
- 팀원들의 파일 작업 조율에 도움을 줌

## Git 작업 요약

![Working tree, staging area, and Git directory.](https://git-scm.com/book/en/v2/images/areas.png)

1. 파일 작업 (Working Directory, 1통)
2. git add (Staging Area, 2통)
3. git commit 

## Git 파일 생명 주기

![파일의 라이프사이클.](https://git-scm.com/book/en/v2/images/lifecycle.png)

- Tracked : 버전으로 관리되고 있는 상태
  - Unmodified : 커밋이 완료되어 git status에 나타나지 않음
  - Modified : 커밋했던 파일이 수정된 상태
  - Staged : 곧 커밋이 이루어질 상태

- Untracked : 관리되지 않고 있는 상태

## Git 기본 명령어

- **git init** : 로컬 저장소 생성
- **git add <파일명>** : 특정 파일/폴더의 변경 사항 추가
- **git commit -m '<메시지>'** : 커밋(버전 기록)

- **git log** : 현재 저장소에 기록된 커밋 내역 조회
  - git log -1 : 가장 최근 커밋 내역 조회
  - git log --oneline : 커밋 내역 1줄로 조회
  - git log -p : 커밋 내역 상세 조회
  - 각 인자들은 중첩 사용 가능 (ex : git log -p --online)

- **git status** : 현재 저장소에 있는 파일의 상태 확인
  - Untracked file (추적 중이지 않음)
  - Changes not staged for commit (Tracked 상태이지만 Staged 상태는 아님)
  - Changes to be committed (Staged 상태)
  - Noting to commit, working tree clean (파일을 하나도 수정하지 않아 커밋을 할 파일이 없는 상태)

- **git config --global user.name "<이름>"** : 커밋을 위한 사용자 이름 설정
- **git config --global user.email "<이메일>"** : 커밋을 위한 사용자 이메일 설정
- **git config --global core.editor "code --wait"** : VS Code를 에디터로 활용
- **git config --global --list** : 설정 확인

- **git remote add <원격\_저장소\_이름 (주로 *origin*으로 설정)> <원격\_저장소\_주소>** : 원격 저장소 정보를 로컬 저장소에 연동하는 과정
- **git remote -v** : 원격 저장소의 정보 확인
- **git push <원격\_저장소\_이름> <브랜치\_이름>** : 로컬 저장소의 변경 사항(커밋)을 원격 저장소로 보내기
- **git pull  <원격\_저장소\_이름> <브랜치\_이름>** : 원격 저장소에서 변경 내역을 받아서 이력 병합
- **git clone <원격\_저장소\_주소>** : 원격 저장소를 로컬 저장소로 복제하여 모든 버전을 가져옴

## .gitignore

- 버전 관리를 별도로 할 필요가 없는 파일 및 폴더를 기록하여 git status 목록에서 제외함
- **반드시 프로젝트 시작 전에 미리 설정해야 함! (이미 커밋된 파일은 삭제해야 적용되기 때문)**

## 참고 문헌

[Git - Book (git-scm.com)](https://git-scm.com/book/ko/v2)
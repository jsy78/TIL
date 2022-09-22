# 들어가기 전에...

| (1통)                | add | (2통) | commit | (로컬 저장소) | push or pull | (원격 저장소) |
| :------------------: | :--:    | :--: | :--: | :--:|:--: | :--:|
| Working Directory | \-----> |Staging Area| \-----> | Local Repository | <\-----> | Remote Repository |

- git status (파일, 폴더 상태)와 git log (커밋 기록)를 수시로 확인하자.
- git restore [file name]을 사용해 특정 파일 HEAD Commit으로 복구할 수 있다.
- git restore --source [commit hash] [file name]로 특정 파일을 특정 Commit 시점으로 복구할 수 있다.
- git restore --staged [file name]로 특정 파일 add를 취소할 수 있다.
- git은 우리 생각보다 아주 친절하니 에러가 발생하면 메시지를 잘 읽자.

# Git Flow

- Git을 활용하여 협업하는 흐름으로 **branch**를 활용하는 전략
- 기본 원칙
  - master branch는 반드시 배포 가능한 상태여야 함
  - feature branch는 각 기능의 의도를 알 수 있도록 작성
  - commit message는 **매우** 중요하며, 명확하게 작성
  - pull request를 통해 협업 진행
  - 변경 사항을 반영하고 싶다면 master branch에 병합


## 주요 branch 종류

- **main**
  - **master** : **배포 가능한 상태**의 코드
  - **develop** : 버그 수정 등 개발 진행
- **supporting**
  - **feature branches** : 기능 별로 개발 진행, 기능이 반영되거나 드랍되면 삭제
  - **release branches** : 개발 완료 이후 QA/Test 등을 통해 얻어진 다음 배포 전 마이너 버그 픽스 등 반영
  - **hotfixes** : 현재 버전에 긴급하게 반영해야 하는 버그 픽스

## branch 관련 명령어

- ```bash
  (master) $ git branch {branch name}
  # 브랜치 생성
  ```

- ```bash
  (master) $ git checkout {branch name}
  # 브랜치 이동
  ```

- ```bash
  (master) $ git checkout -b {branch name}
  # 브랜치 생성 및 이동
  ```

- ```bash
  (master) $ git branch
  # 브랜치 목록
  ```

- ```bash
  (master) $ git branch -d {branch name}
  # 브랜치 삭제

- ```bash
  (master) $ git merge {branch name}
  # {branch name} 브랜치를 master 브랜치에 병합
  # 충돌이 발생하여 자동으로 병합되지 않으면 직접 수정하고 다시 add, commit을 해야 함
  ```

## branch workflow

### Feature branch workflow

- 각 사용자가 저장소의 소유권을 가지고 있는 경우

- 진행 방식
  1. 각 사용자는 clone을 통해 원격 저장소를 로컬로 복제
  2. 각 사용자는 기능 추가를 위해 로컬에 branch를 생성하고 기능을 구현
  3. 기능 구현 후 원격 저장소에 각 branch를 push하여 원격 저장소에 반영
  4. 원격 저장소에 쌓인 branch를 pull request로 병합
  5. 병합 완료된 원격 저장소의 branch는 삭제
  6. 각 사용자는 master branch로 checkout
  7. 병합된 원격 저장소의 master branch 내용을 pull하여 가져옴
  8. 원격 master의 내용이 로컬 master에 반영되면 로컬 branch는 삭제
  9. 새로운 기능을 추가하고자 하면 다시 2번으로 돌아가 반복

### Forking workflow

- 저장소의 소유권이 없는 경우

- 진행 방식

  1. 소유권이 없는 원격 저장소를 fork를 통해 자신의 원격 저장소로 복제

  2. 본인의 계정에 있는 fork한 원격 저장소(origin)를 clone하여 로컬로 복제

  3. 기능 추가를 위해 로컬에 branch를 생성하고 기능을 구현

  4. 기능 구현 후 **본인** 계정의 원격 저장소에 push하여 반영
  
     (git push **origin** feature)
  
  5. 원본 소유자에게 pull request를 보냄
  
  6. 원본에 병합이 완료되면 자신의 원격 저장소에 push된 branch 삭제
  
  7. 로컬 저장소에서 master branch로 checkout
  
  8. 원본 원격 저장소와 연결
  
     (git remote add **upstream** [원본 URL])
  
  9. 병합된 원본 원격 저장소의 master 내용을 pull
  
     (git pull **upstream** master)
  
  10. 원격 master의 내용이 로컬 master에 반영되면 로컬 branch는 삭제
  
  11. 새로운 기능을 추가하고자 하면 다시 3번으로 돌아가 반복

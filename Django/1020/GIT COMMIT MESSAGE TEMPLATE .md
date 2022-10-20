# GIT COMMIT MESSAGE TEMPLATE

1️⃣ 템플릿을 적용할 git 프로젝트에 **`.gitmessage.txt`** 생성


![Untitled](./GIT%20COMMIT%20MESSAGE%20TEMPLATE/Untitled.png)

2️⃣ 템플릿 내용 작성(**`.gitmessage.txt`**)


```
################
# <타입> : <제목> 의 형식으로 제목을 아래 공백줄에 작성
# 제목은 50자 이내 / 변경사항이 "무엇"인지 명확히 작성 / 끝에 마침표 금지
# 예) feat : 로그인 기능 추가

# 바로 아래 공백은 지우지 마세요 (제목과 본문의 분리를 위함)

################
# 본문(구체적인 내용)을 아랫줄에 작성
# 여러 줄의 메시지를 작성할 땐 "-"로 구분 (한 줄은 72자 이내)

################
# feat : 새로운 기능 추가
# fix : 버그 수정
# docs : 문서 수정
# test : 테스트 코드 추가
# refact : 코드 리팩토링
# style : 코드 의미에 영향을 주지 않는 변경사항
# chore : 빌드 부분 혹은 패키지 매니저 수정사항
################
```

3️⃣ 명령어 입력


```bash
# 커밋 메세지 템플릿 적용 명령어
git config --local commit.template .gitmessage.txt

# 깃 커밋 메세지를 vscode에서 작성하기 위한 설정
git config --local core.editor "code --wait"
```

4️⃣ git add / git commit


```bash
git add .

# -m 옵션 없이 commit만 입력
git commit 
```

5️⃣ `COMMIT_EDITMSG` 파일에 메세지 작성 후 저장 & 파일 닫기
이후 자동으로 commit 완료 됨


![Untitled](./GIT%20COMMIT%20MESSAGE%20TEMPLATE/Untitled%201.png)
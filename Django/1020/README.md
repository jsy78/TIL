# 장고 16

Date: 2022년 10월 20일

# 실습

## 목표

1. ModelForm을 활용한 CRUD 구현
2. Django Model 1 : N 관계를 매핑하고, View에서 서로 참조해서 사용하기
    1. 유저 : 게시글 = 1 : N
    2. 유저 : 댓글 = 1 : N
    3. 게시글 : 댓글 = 1 : N
3. Django Auth를 활용한 회원 관리 기능 개발에 대한 흐름 파악 및 개발
4. 로그인 상태에 따라 컴포넌트 출력 및 기능 제한
5. Django Media 활용 정적 파일 다루기

## 요구사항

### 모델 Model

모델은 아래 조건을 만족해야합니다.

- 모델 이름 : User
  
    Django **AbstractUser** 모델 상속
    
- 모델 이름 : Article
  
    모델 필드
    
    | 필드 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | user | 글 작성자 | ForeignKey | on_delete=models.CASCADE |
    | title | 글 제목 | Char | max_length=80 |
    | content | 글 내용 | Text |  |
    | image | 글 이미지 | Image | upload_to=”articles/” |

- 모델 이름 : Comment
  
    모델 필드
    
    | 필드 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | user | 댓글 작성자 | ForeignKey | on_delete=models.CASCADE |
    | article | 게시글 | ForeignKey | on_delete=models.CASCADE |
    | content | 댓글 내용 | Char | max_length=80 |

---

### 기능 View

**게시판 articles** 

데이터 목록 조회

- `GET` http://127.0.0.1:8000/article**s**/

데이터 정보 조회

- `GET` http://127.0.0.1:8000/article**s**/<int:article_pk>/
- 해당 게시글(int:article_pk)의 댓글 목록 조회

데이터 생성

- `POST` http://127.0.0.1:8000/article**s**[/](http://127.0.0.1:8000/posts/create/)create[/](http://127.0.0.1:8000/posts/create/)
- 로그인한 사용자만 데이터를 생성할 수 있습니다.

데이터 수정

- `POST` http://127.0.0.1:8000/article**s**/<int:article_pk>/update/
- 데이터를 생성한 사용자만 수정할 수 있습니다.

데이터 삭제

- `POST` http://127.0.0.1:8000/article**s**/<int:article_pk>/delete/
- 데이터를 생성한 사용자만 삭제할 수 있습니다.

**댓글 comments**

게시글 댓글 목록 조회

- `GET` http://127.0.0.1:8000/article**s**/<int:article_pk>/
- 해당 게시글의 댓글 목록을 조회합니다.

댓글 생성

- `POST` http://127.0.0.1:8000/article**s**/<int:articles_pk>/comments/create/
- 로그인한 사용자만 데이터를 생성할 수 있습니다.

댓글 삭제

- `POST` http://127.0.0.1:8000/article**s**/<int:articles_pk>/comments/<int:comment_pk>/delete/
- 데이터를 생성한 사용자만 삭제할 수 있습니다.

회원 관리 accounts 

회원가입

- `POST` http://127.0.0.1:8000/accounts/signout/

로그인

- `POST` http://127.0.0.1:8000/accounts/login/

로그아웃

- `POST` http://127.0.0.1:8000/accounts/logout/
- 사용자 로그아웃

회원 정보 조회

- `GET` http://127.0.0.1:8000/accounts/<int:user_pk>/
- 회원이 작성한 게시글 목록을 출력합니다.
- 회원이 작성한 댓글 목록을 출력합니다.

---

### 화면 Template

게시글 목록 페이지

- `GET` http://127.0.0.1:8000/article**s/**

게시글 정보 페이지

- `GET` http://127.0.0.1:8000/articles/<int:article_pk>/
- 해당 게시글 정보 출력
    - 게시글 작성자(username) 클릭 시 해당 회원 조회 페이지로 이동
- 댓글 컴포넌트
    - 댓글 작성 폼
        - 로그인한 사용자에게만 보여야합니다.
    - 댓글 개수
    - 댓글 목록
        - 댓글 내용
        - 댓글 삭제 버튼
            - 댓글을 작성한 사용자에게만 보여야합니다.

게시글 작성 페이지

- `GET` http://127.0.0.1:8000/article**s**/create/
- 로그인 한 사용자만 글 작성 페이지로 진입할 수 있습니다.
- 게시글 작성 폼

로그인 페이지

- `GET` http://127.0.0.1:8000/accounts/login/
- 로그인 폼
- 회원가입 페이지 이동 버튼

회원가입 페이지

- `GET` http://127.0.0.1:8000/accounts/signup/
- 회원가입 폼
- 로그인 페이지 이동 버튼

회원 조회 페이지(프로필 페이지)

- `GET` http://127.0.0.1:8000/accounts/<int:user_pk>/
- 회원이 작성한 게시글 목록 출력
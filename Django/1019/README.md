# 장고 15

Date: 2022년 10월 19일

---

# 실습

[GitHub - agusmakmun/django-markdown-editor: Awesome Django Markdown Editor, supported for Bootstrap & Semantic-UI](https://github.com/agusmakmun/django-markdown-editor)

## 목표

1. ModelForm을 활용한 CRUD 기능 구현
2. Django Model 1 : N 관계에 대해 이해하고, 코드 상에서 두 모델 매핑하기
3. Django Auth를 활용한 회원 관리 기능 개발에 대한 흐름 파악 및 개발
4. 로그인 상태에 따라 컴포넌트 출력 및 기능 제한

## 요구사항

### 모델 Model

- 모델 이름 : User
  
    Django **AbstractUser** 모델 상속
    
- 모델 이름 : Article
  
    모델 필드
    
    | 필드 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | user | 글 작성자 | ForeignKey | on_delete=models.CASCADE |
    | title | 글 제목 | Char | max_length=80 |
    | content | 글 내용 | Text |  |

### **폼 Form**

로그인

- Django 내장 로그인 폼 **AuthenticationForm** 활용

### 기능 View

데이터 목록 조회

- `GET` http://127.0.0.1:8000/article**s**/

데이터 정보 조회

- `GET` http://127.0.0.1:8000/article**s**/<int:article_pk>/

데이터 생성

- `POST` http://127.0.0.1:8000/article**s**[/](http://127.0.0.1:8000/posts/create/)create[/](http://127.0.0.1:8000/posts/create/)
- 로그인한 사용자만 데이터를 생성할 수 있습니다.

회원 관리 accounts

회원 가입은 python manage.py createsuperuser 명령어로 대체

로그인

- `POST` http://127.0.0.1:8000/accounts/login/

로그아웃

- `POST` http://127.0.0.1:8000/accounts/logout/
- 사용자 로그아웃

회원 정보 조회

- `GET` http://127.0.0.1:8000/accounts/<int:user_pk>/
- 회원이 작성한 글 목록 출력

### 화면 Template

게시글 목록 페이지

- `GET` http://127.0.0.1:8000/article**s/**

게시글 정보 페이지

- `GET` http://127.0.0.1:8000/articles/<int:article_pk>/
- 해당 게시글 정보 출력
    - 게시글 작성자(username) 클릭 시 해당 회원 조회 페이지로 이동

게시글 작성 페이지

- `GET` http://127.0.0.1:8000/article**s**/create/
- 로그인 한 사용자만 글 작성 페이지로 진입할 수 있습니다.
- 게시글 작성 폼

로그인 페이지

- `GET` http://127.0.0.1:8000/accounts/login/
- 로그인 폼
- 회원가입 페이지 이동 버튼

회원 조회 페이지(프로필 페이지)

- `GET` http://127.0.0.1:8000/accounts/<int:user_pk>/
- 회원이 작성한 게시글 목록 출력
# 장고 19

Date: 2022년 10월 26일

---

## 실습

### 목표

1. JavaScript  비동기 처리에 대해 학습합니다. 아래 내용을 중점적으로 학습합니다.
    1. 비동기 처리 필요성
    2. 비동기 처리 원리와 과정
    
    [자바스크립트 비동기 처리와 콜백 함수](https://joshua1988.github.io/web-development/javascript/javascript-asynchronous-operation/)
    
    [[자바스크립트] 비동기 처리 1부 - Callback](https://www.daleseo.com/js-async-callback/)
    
2. 댓글 기능을 비동기로 처리합니다.
    1. 생성
    2. 삭제

### 요구사항

#### 모델 Model

모델은 아래 조건을 만족해야합니다.

- 모델 이름 : Article
  
    모델 필드
    
    | 필드 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | title | 글 제목 | Char | max_length=80 |
    | content | 글 내용 | Text |  |
    |  |  |  |  |

- 모델 이름 : Comment
  
    모델 필드
    
    | 필드 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | content | 댓글 내용 | Char | max_length=80 |
    | article | 게시글 | ForeignKey | on_delete=models.CASCADE |

#### 기능 View

**게시판 articles** 

게시글 목록 조회

- `GET` http://127.0.0.1:8000/articles/

게시글 정보 조회

- `GET` http://127.0.0.1:8000/articles/<int:article_pk>/
- 해당 게시글(article_pk)에 작성된 댓글 목록 조회

게시글 생성

- `POST` http://127.0.0.1:8000/articles[/](http://127.0.0.1:8000/posts/create/)create[/](http://127.0.0.1:8000/posts/create/)

**댓글 comments**

게시글에 작성된 댓글 목록 조회

- `GET` http://127.0.0.1:8000/articles/<int:article_pk>/
- 해당 게시글(article_pk)의 댓글 목록 조회

댓글 생성

- `POST` http://127.0.0.1:8000/articles/<int:article_pk>/comments/
- 비동기 처리

댓글 삭제

- `POST` http://127.0.0.1:8000/articles/<int:article_pk>/comments/<int:comment_pk>/delete/
- 비동기 처리

#### 화면 Template

게시글 목록 페이지

- `GET` http://127.0.0.1:8000/articles/

게시글 정보 페이지

- `GET` http://127.0.0.1:8000/articles/<int:article_pk>/
- 댓글 작성 폼
- 댓글 목록
    - 댓글 내용
    - 댓글 삭제 버튼

게시글 작성 페이지

- `GET` http://127.0.0.1:8000/articles/create/
- 게시글 작성 폼
# 장고 14

Date: 2022년 10월 18일

---

# 실습

## 목표

게시글과 댓글이 **1 : N** 관계로 매핑 된 게시글에 댓글을 작성할 수 있는 서비스를 개발합니다.

## 요구사항

### 모델 Model

모델은 아래 조건을 만족해야합니다.

- 모델 이름 : Article
  
    모델 필드
    
    | 필드 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | title | 글 제목 | Char | max_length=80 |
    | content | 글 내용 | Text |  |

- 모델 이름 : Comment
  
    모델 필드
    
    | 필드 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | article | 참조 게시글 | ForeignKey | on_delete=models.CASCADE |
    | content | 댓글 내용 | Char | max_length=80 |

### 기능 View

**게시판 articles** 

게시글 목록 조회

- `GET` `http://127.0.0.1:8000/articles/`

게시글 정보 조회

- `GET` `http://127.0.0.1:8000/articles/<int:article_pk>/`
- 해당 게시글(article_pk)에 작성된 댓글 목록 조회

게시글 생성

- `POST` `http://127.0.0.1:8000/articles/create/`

**댓글 comments**

게시글에 작성된 댓글 목록 조회

- `GET` `http://127.0.0.1:8000/articles/<int:article_pk>/`
- 해당 게시글(article_pk)의 댓글 목록 조회

댓글 생성

- `POST` `http://127.0.0.1:8000/articles/<int:article_pk>/comments/`

댓글 삭제 **(교재 참고)**

- `POST` `http://127.0.0.1:8000/articles/<int:article_pk>/comments/<int:comment_pk>/delete/`

### 화면 Template

게시글 목록 페이지

- `GET` `http://127.0.0.1:8000/articles/`

게시글 정보 페이지

- `GET` `http://127.0.0.1:8000/articles/<int:article_pk>/`
- 댓글 작성 폼
- 총 댓글 개수 출력 **(교재 참고)**
- 댓글 목록
    - 댓글 내용
    - 댓글 삭제 버튼 **(교재 참고)**

게시글 작성 페이지

- `GET` `http://127.0.0.1:8000/articles/create/`
- 게시글 작성 폼
# 장고 17

Date: 2022년 10월 24일

---

# 실습


## 목표

이전에 진행한 실습에 **유저(User)와 게시글(Article)**이 **N : M** 관계로 매핑된 좋아요 기능을 추가로 개발합니다.


## 요구사항

### 모델 Model

- 모델 이름 : User
  
    Django AbstractUser 모델 상속
    
- 모델 이름 : Article
  
    모델 필드
    
    | 필드 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | title | 글 제목 | Char | max_length=20 |
    | content | 글 내용 | Text |  |
    | user | 글 작성자 | ForeignKey | on_delete=models.CASCADE |
    | like_users | 좋아요 | ManyToMany | related_name='like_articles’ |

### 기능 View

**게시판 articles** 

게시글 좋아요 & 좋아요 취소

- `POST` http://127.0.0.1:8000/articles/<int:article_pk>/likes/
- 로그인한 유저만 좋아요를 할 수 있습니다.

### 화면 Template

게시글 정보 페이지

- `GET` http://127.0.0.1:8000/articles/<int:article_pk>/
- 좋아요 버튼
  
    해당 글이 받은 좋아요 수를 표시합니다.
    
    로그인 상태와 좋아요 상태에 따라 다르게 표현하고, 기능을 제한합니다.
    
    각 버튼 예시
    
    ![Untitled](./README.assets/Untitled.png)
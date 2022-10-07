# 페어 프로그래밍 2

Date: 2022년 10월 7일

---

## 오늘의 일정

```
⏰ ~ 12: 00 - 페어 프로그래밍
~ 13 : 30 - 점심 시간
~ 17 : 50 - 페어 프로그래밍
~ 18 : 00 - 마무리
```

## 목표

페어 프로그래밍을 통한 영화 리뷰 커뮤니티 서비스를 개발합니다. 아래 조건을 만족해야합니다.

- ModelForm 활용 CRUD 구현
- Staticfiles 활용 서비스 로고 표시

## 요구 사항

### 모델 Model

모델은 아래 조건을 만족해야합니다. 

적절한 필드와 속성을 부여하세요.

- 모델 이름 : Review
- 모델 필드
  
  
    | 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | title | 리뷰 제목 |  |  |
    | content | 리뷰 내용 |  |  |
    | movie_name | 영화 이름 |  |  |
    | grade | 영화 평점 |  |  |
    | created_at | 리뷰 생성시간 | DateTime | auto_now_add=True |
    | updated_at | 리뷰 수정시간 | DateTime | auto_now = True |

### 기능 View

아래 작성된 기능을 구현합니다.

생성 및 수정은 ModelForm을 사용하여 구현합니다.

- 데이터 목록 조회
    - `GET` http://127.0.0.1:8000/reviews/
- 데이터 정보 조회
    - `GET` http://127.0.0.1:8000/reviews/<int:pk>/
- 데이터 생성
    - `POST` http://127.0.0.1:8000/reviews/create/
    
    사용자에게 아래 데이터를 입력 받습니다.
    
    - 리뷰 제목
    - 리뷰 내용
    - 영화 이름
    - 영화 평점
- 데이터 수정
    - `POST` http://127.0.0.1:8000/reviews/<int:pk>/update/
- 데이터 삭제
    - `POST` http://127.0.0.1:8000/reviews/<int:pk>/delete/

### 화면 Template

아래 작성된 페이지를 구현합니다.

**네비게이션바, Bootstrap \<nav>**

- 서비스 로고
    - Django Staticfiles 활용
    - 클릭 시 메인 페이지로 이동
- 리뷰 목록 버튼
    - 클릭 시 목록 페이지로 이동
- 리뷰 작성 버튼
    - 클릭 시 작성 페이지로 이동

**메인 페이지**

- `GET` http://127.0.0.1:8000/reviews/
- 자유 디자인

목록 페이지

- `GET` http://127.0.0.1:8000/reviews/index/
- 리뷰 목록 출력
    - 리뷰 제목
    - 영화 이름
- 제목을 클릭하면 해당 리뷰의 정보 페이지로 이동

**리뷰 정보 페이지**

- `GET` http://127.0.0.1:8000/reviews/<int:pk>/
- 해당 리뷰 정보 출력
- 수정 / 삭제 버튼

**리뷰 작성 페이지**

- `GET` http://127.0.0.1:8000/reviews/create/
- 리뷰 작성 폼

**리뷰 수정 페이지**

- `GET` http://127.0.0.1:8000/reviews/<int:pk>/update/
- 리뷰 수정 폼
# 장고 13

Date: 2022년 10월 17일

---

# 실습


복습 자료

Django Media

[Managing files | Django documentation | Django](https://docs.djangoproject.com/en/4.1/topics/files/)

Django imagekit

[https://github.com/matthewwithanm/django-imagekit](https://github.com/matthewwithanm/django-imagekit)

[썸네일 만들기 (PILKit, imagekit) ImageSpecField, ProcessedImageField](https://wayhome25.github.io/django/2017/05/11/image-thumbnail/)

Django Message Framework

[The messages framework | Django documentation | Django](https://docs.djangoproject.com/en/4.1/ref/contrib/messages/)

Django Widget Tweaks

[django-widget-tweaks](https://pypi.org/project/django-widget-tweaks/)

## 목표

Django Media를 활용한 이미지 업로드가 가능한 게시판 서비스를 개발합니다.

## 요구사항

### 모델 Model

- 모델 이름 : Article
  
    적절한 필드 속성을 설정합니다.
    
    모델 필드
    
    | 필드 이름 | 역할 | 필드 | 속성 |
    | --- | --- | --- | --- |
    | title | 글 제목 | Char |  |
    | content | 글 내용 | Text |  |
    | image | 글 이미지 | Image |  |
    | thumbnail | 썸네일 이미지 | ProcessedImage |  |

### 기능 View

데이터 목록 조회

- `GET` http://127.0.0.1:8000/article**s**/

데이터 정보 조회

- `GET` http://127.0.0.1:8000/article**s**/<int:pk>/

데이터 생성

- `POST` http://127.0.0.1:8000/article**s**/create/
- 사용자가 글 이미지 `image`와 썸네일 이미지 `thumbnail` 를 업로드할 수 있어야합니다.

데이터 수정

- `POST` http://127.0.0.1:8000/article**s**/<int:pk>/update/

데이터 삭제

- `POST` http://127.0.0.1:8000/article**s**/<int:pk>/delete/

### 화면 Template

목록 페이지

- `GET` http://127.0.0.1:8000/article**s**/
- 게시글 목록
- 썸네일 이미지 `thumbnail`가 있으면 썸네일 이미지를 출력합니다.

정보 페이지

- `GET` http://127.0.0.1:8000/article**s**/<int:pk>/
- 해당 게시글 정보 출력
    - 글 이미지 `image` 가 있으면 이미지를 출력합니다.

작성 페이지

- `GET` http://127.0.0.1:8000/article**s**/create/
- 게시글 작성 폼
    - 사용자가 이미지를 업로드할 수 있어야합니다.

수정 페이지

- `GET` http://127.0.0.1:8000/article**s**/<int:pk>/update/
- 게시글 수정 폼
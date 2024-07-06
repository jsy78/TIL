# 프로젝트 기획

## 프로젝트 개요

```
❓ 역할별 할일
팀장 : 스크럼 진행 / 스크럼 일지 제출 / 팀 내 특이사항 공유
발표자 : 프로젝트 발표
PPT 제작자 : 프로젝트 발표회에 사용할 PPT 제작
```

| 프로젝트 목적 | 웹 프레임워크 Django와 HTML / CSS / JavaScript를 활용한 콘텐츠 기반 커뮤니티 웹 플랫폼 개발 |
| --- | --- |
| 프로젝트 기간 | 10.31 (월) ~ 11.07 (월) |
| 발표 날짜 | 11.08 (화) |
| 팀명 | 맛팔해조 |
| 주제 | 맛집 정보 및 후기 공유 커뮤니티 서비스 |
| 팀장 | 조성윤 |
| 발표자 | 강동현 |
| PPT 제작자 | 장성민 |
| PPT 제작자 | 임선주 |

## 개발 역할 분담


<img src="https://www.notion.so/icons/meeting_gray.svg" alt="https://www.notion.so/icons/meeting_gray.svg" width="40px" /> 
```
개발 영역에서 주로 담당할 업무를 정합니다.
아래의 역할 분담은 주 업무일 뿐입니다.
모든 업무는 모든 팀원의 업무입니다.
```

| 이름 | 역할 |
| --- | --- |
| 강동현 | 프로젝트 베이스 코드 작성, 백엔드 개발 |
| 조성윤 | 콘텐츠 데이터 수집, 백엔드 개발 |
| 장성민 | 화면 설계, 프론트엔드 개발 |
| 임선주 | 화면 설계, 프론트엔드 개발 |

## 주제 사전 조사 & 분석

```
🔎 선택한 주제와 유사한 서비스를 조사하고 분석합니다.
참고할 사이트와 자료를 기록합니다.
```

[망고플레이트: 나만의 맛집 검색](https://www.mangoplate.com/)

[빅데이터 맛집검색, 다이닝코드](https://www.diningcode.com/)

[식신 : 대한민국 No.1 맛집검색,맛집추천](https://www.siksinhot.com/)

[디너의여왕 - 푸드 분야 국내 1위 마케팅 플랫폼](https://dinnerqueen.net/)

[POING](https://m.poing.io/)

[발 빠른 미식 플랫폼, 뽈레!](https://polle.com/)

## 서비스 주요 기능

```
⚙️ 프로젝트 필수 사항과 사전 조사를 기반으로 서비스의 주요 기능(MTV)을 작성합니다.
```

- **회원관리**
    - 회원가입
    - 로그인
    - 로그아웃
    - 회원 프로필
        - 프로필 사진
        - 비번 수정
        - 회원정보 수정
        - 작성한 글 / 댓글
        - 스크랩한 글
        - 좋아요한 글
    - 팔로우

- **메인**
    - 최신순/후기많은순/인기순(좋아요 많은)으로 재정렬
    - 조회수/좋아요수
    - navbar(header)
    - navbar(footer)
    - 검색 > 해시태그 (희망사항)

- **게시글(맛집후기글)**
    - 작성
        - 이미지 첨부
        - 썸네일 첨부
        - 평점
        - 해시태그 (희망사항)
        - rich text editor 활용 (희망사항)
    - 수정
    - 삭제
    - 추천 (좋아요)
    - 스크랩 (저장)
    - 상세보기
        - 지도
    
- **댓글**
    - 작성
    - 수정(작성자만)
    - 삭제
    - 추천 (좋아요)
    - 대댓글

## 화면 설계

```
🎨 PPT / 피그마 / 카카오 오븐 등의 도구를 활용해서 화면을 설계 합니다.
최소 페이지의 레이아웃은 설계합니다.
```

![Untitled.png](./선택%20프로젝트%20I%20기획/Untitled.png)

![Untitled2.png](./선택%20프로젝트%20I%20기획/Untitled2.png)

![Untitled3.png](./선택%20프로젝트%20I%20기획/Untitled3.png)

## DB 모델링(ERD)

```
🧾 서비스를 구현하기 위한 데이터베이스의 ERD를 작성합니다. 
```
ERD 작성 사이트
[https://app.diagrams.net](https://app.diagrams.net/)
[https://www.erdcloud.com](https://www.erdcloud.com/)
[https://dbdiagram.io/home?utm_source=holistics&utm_medium=rails_erd_blog](https://dbdiagram.io/home?utm_source=holistics&utm_medium=rails_erd_blog)


![모델링.png](./선택%20프로젝트%20I%20기획/ERD.png)
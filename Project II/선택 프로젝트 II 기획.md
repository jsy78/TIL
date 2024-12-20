# 프로젝트 기획

## 프로젝트 개요

| 프로젝트 목적 | 웹 프레임워크 Django와 HTML / CSS / JavaScript를 활용한 콘텐츠 기반 커뮤니티 웹 플랫폼 개발 |
| --- | --- |
| 프로젝트 기간 | 11.09 (수) ~ 11.21 (월) |
| 발표 날짜 | 11.22 (화) |
| 팀명 | 별다방 |
| 주제 | 맛집 정보 및 후기 공유 커뮤니티 서비스 |
| 팀장 | 조성윤 |
| 발표자, 서기 | 배서림 |
| PPT 제작자 | 김나현, 김희동, 손세철 |

## 개발 역할 분담

| 이름 | 역할 |
| --- | --- |
| 김나현 | 백엔드, DB 모델링 |
| 김희동 | 프론트엔드, DB 모델링 |
| 배서림 | 프론트엔드, DB 모델링 |
| 손세철 | 프론트엔드, DB 모델링 |
| 조성윤 | 백엔드, DB 모델링 |

## 주제 사전 조사 & 분석

[망고플레이트: 나만의 맛집 검색](https://www.mangoplate.com/)

[빅데이터 맛집검색, 다이닝코드](https://www.diningcode.com/)

[식신 : 대한민국 No.1 맛집검색,맛집추천](https://www.siksinhot.com/)

[디너의여왕 - 푸드 분야 국내 1위 마케팅 플랫폼](https://dinnerqueen.net/)

[POING](https://m.poing.io/)

[발 빠른 미식 플랫폼, 뽈레!](https://polle.com/)

http://www.aboutcafe.co.kr/

## 서비스 주요 기능

필수

미정

- 목차
    1. 주요 참고 사이트
    2. 회원 관리
    3. 메인
    4. 게시글 (맛집)
    5. 게시글 (후기)
    6. 댓글
    
1. 주요 참고 사이트

[식신 : 대한민국 No.1 맛집검색,맛집추천](https://www.siksinhot.com/)

1. 회원 관리

| 주요 기능 | 기능 세부 |
| --- | --- |
| 회원가입 | SNS 회원가입 |
| 로그인 | SNS 로그인 |
| 로그아웃 |  |
| 회원 프로필 | 프로필 사진
비밀번호 수정
회원 정보 수정
회원 탈퇴
주요 활동 지역
작성한 글 / 댓글
즐겨찾기 한 글
좋아요 한 글
나를 위한 추천 |
| 팔로우 | 팔로우 기능
팔로우 수 확인
팔로워 수 확인 |

1. 메인

| 주요 기능 | 기능 세부 |
| --- | --- |
| navbar(header) | 메인 페이지로 돌아가기
검색창
카테고리 (맛집 찾기, 테마별 맛집)
회원 관리창 |
| 주요 화면 | 홍보 캐러셀 (안에 뭐 넣을지 생각해봐야 함)
인기순 / 후기순 / (최신순) 정렬
테마별 맛집
테마별 맛집의 ‘더보기’ 기능 |
| navbar(footer) | 만든 사람들 이름
카피라이트
사이트 관련 SNS 링크 |

1. 게시글 (맛집)

| 주요 기능 | 기능 세부 |
| --- | --- |
| 정보 | 이름
평점
길찾기
조회수
음식 사진
지역 / 주소
지도
업종
전화번호
영업 시간
주차 정보
메뉴
가격대
포털 정보
정보 수정
리뷰 작성 (아래 맛집 후기글)
좋아요
공유하기
주변 추천 맛집
이 맛집이 소개된 테마 |

1. 게시글 (후기)

| 주요 기능 | 기능 세부 |
| --- | --- |
| 작성 | 이미지 첨부(multi image)
평점
해시태그
rich text editor 활용 |
| 수정 | 수정 완료 메시지 |
| 삭제 | 삭제 재확인 모달 또는 메시지 |
| 평점 | 평점 평균값 |
| 좋아요(추천) | 좋아요 유무
좋아요 갯수 |
| 스크랩 | URL 저장 |
| 상세보기 | 위치(지도)
상세 정보 |

1. 댓글

| 주요 기능 | 기능 세부 |
| --- | --- |
| 작성 | 작성 시간 |
| 삭제 |  |
| 수정 |  |
| 대댓글 |  |
| 댓글 좋아요 |  |
| 댓글에서 프로필 정보 | 댓글 작성자 프로필로 이동 |

## DB 모델링(ERD)

[선택 프로젝트 II](https://www.erdcloud.com/d/RbGaBFTTN9tycRBWe)

![별다방.png](./선택%20프로젝트%20II%20기획/1.png)

## 장고 모델(Model) 설계

```
💽 데이터베이스를 장고 모델 형태로 설계합니다.
설계를 기반으로 장고 모델 코드를 작성합니다.
```

[model.csv](./선택%20프로젝트%20II%20기획/model.csv)

## 장고 기능(View) 설계

```
⚙ 구현 할 기능들을 설계합니다.
설계를 기반으로 기능 개발을 진행합니다.
```

[view.csv](./선택%20프로젝트%20II%20기획/view.csv)

 

## 화면 설계

[Untitled](https://www.figma.com/file/4hhOkRZrAzStZMRCVudBMu/Untitled?node-id=0%3A1)

- 메인페이지
  
    ![메인페이지(main).png](./선택%20프로젝트%20II%20기획/2.png)
    
- 메인페이지 (스크롤)
  
    ![메인페이지 스크롤(main).png](./선택%20프로젝트%20II%20기획/3.png)
    
- 메인페이지 (카테고리 누름)
  
    ![게시글 (카테고리 눌렀을 때).png](./선택%20프로젝트%20II%20기획/4.png)
    
- 네브바 펼침 (로그인)
  
    ![메인페이지 네브바 펼침 (main) - 로그인.png](./선택%20프로젝트%20II%20기획/5.png)
    
- 네브바 펼침 (로그아웃)
  
    ![메인페이지 네브바 펼침 (main) - 로그아웃.png](./선택%20프로젝트%20II%20기획/6.png)
    
- 게시글 (카테고리 내의 글을 누름)
  
    ![게시글 (카페를 눌러서 이동).png](./선택%20프로젝트%20II%20기획/7.png)
    
- 카페 등록/업데이트
  
    ![업데이트.png](./선택%20프로젝트%20II%20기획/8.png)
    
- 리뷰 등록/업데이트
  
    ![업데이트.png](./선택%20프로젝트%20II%20기획/9.png)
    
- 로그인
  
    ![로그인.png](./선택%20프로젝트%20II%20기획/10.png)
    
- 회원가입
  
    ![회원가입.png](./선택%20프로젝트%20II%20기획/11.png)
    
- 회원 정보 수정
  
    ![회원 정보 수정.png](./선택%20프로젝트%20II%20기획/12.png)
    
- 회원 정보
  
    ![회원 정보.png](./선택%20프로젝트%20II%20기획/13.png)
    
- 상대방이 보는 회원 정보
  
    ![상대방이 보는 회원 정보.png](./선택%20프로젝트%20II%20기획/14.png)
# 웹 02

날짜: 2022년 9월 13일

## 목표

- HTML를 통한 웹 페이지 마크업
- CSS를 통한 선택자 활용 및 속성 부여
- 시맨틱 태그를 활용한 기본 레이아웃 구성
- 영화 추천 사이트 메인 레이아웃 구성

## 준비 사항

1. **(필수)** HTML/CSS 환경 구성
2. **(필수)** Bootstrap

## 요구 사항

### 01_nav_footer.html

![Untitled](./README.assets/Untitled.png)

- navbar 좌측에는 영화 로고가 배치됩니다.
- 항목은 Home, Community, Login로 구성되어 있습니다.
    - Home은 02_home.html으로 링크를 구성합니다.
    - Community는 03_community.html으로 링크를 구성합니다.
    - Login은 Modal이 팝업됩니다.
      
        ![Untitled](./README.assets/Untitled 1.png)
    
- footer는 컨텐츠 최하단에 배치됩니다. 내용은 자유롭게 구성합니다.

### 02_home.html

![Untitled](./README.assets/Untitled-2.png)

- 01_nav_footer.html에서 작성한 Navigation bar & Modal & Footer 코드를 적절한 위치에 사용합니다.
- Carousel을 활용하여 이미지가 자동으로 전환될 수 있도록 합니다.
    - 이미지는 적절한 이미지를 찾아 변경 가능합니다.
- Boxoffice 문구는 `h2` 태그를 활용합니다.
- 영화 목록의 카드 배치는 반응형으로 합니다.
    - Viewport의 가로 크기가 576px 미만일 경우 한 행에 1개씩 표시됩니다.
      
        ![Untitled](./README.assets/Untitled-3.png)
        
    - Viewport의 가로 크기가 576px 이상일 경우 한 행에 2개 이상 표시됩니다.(자유롭게 설정 가능)
      
        ![Untitled](./README.assets/Untitled-4.png)
        
        ![Untitled](./README.assets/Untitled-5.png)
        

### 03_community.html

- 992px 이상
  
    ![Untitled](./README.assets/Untitled-6.png)
    
- 992px 미만
  
    ![Untitled](./README.assets/Untitled-7.png)
    
- 01_nav_footer.html에서 작성한 Navigation bar & Modal & Footer 코드를 적절한 위치에 사용합니다.
- Community 페이지는 크게 게시판 목록과 게시판으로 이루어져 있으며 반응형입니다.
- 게시판 목록(`aside`)은 클릭 가능하지만 연결된 링크는 없습니다.
    - Viewport의 가로 크기가 992px 미만일 경우 HTML main 요소 영역 전체만큼의 너비를 가집니다.
    - Viewport의 가로 크기가 992px 이상일 경우 HTML main 요소 영역 기준으로 좌측 1/6 만큼의 너비를 가집니다.
    - Viewport의 가로 크기 별 반응형 디자인은 스크린 샷 예시를 참고하여 일치하도록 합니다.
- Section (게시판)
    - 게시판은 Viewport의 가로 크기에 따라 전혀 다른 레이아웃으로 구성됩니다.
    - Viewport의 가로 크기가 992px 미만일 경우 게시판은 카드 형식으로 구성됩니다.
    - Viewport의 가로 크기가 992px 이상일 경우 테이블 형식으로 구성되며, HTML main 요소 영역 기준으로 우측 5/6 만큼의 너비를 가집니다.
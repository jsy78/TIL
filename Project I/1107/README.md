
# 🍧 맛팔해조

🔗 [배포 URL](https://glacial-depths-55540.herokuapp.com/)

## 개요

- 🍩 맛팔해조는 음식 맛집에 대한 후기 작성 & 맛집 리스트를 확인하는 서비스입니다.
- 🔍 음식 맛집을 최신 / 인기 / 조회 순으로 정렬, 지역 & 식당 검색이 가능합니다.
- ⭐ 마이페이지에서 작성한 글 / 작성한 댓글 / 좋아요한 글 / 스크랩한 글 / 팔로우한 유저 별로 볼 수 있습니다.
- 💖 피드를 구경하다가 마음에 드는 글(후기)을 발견한다면 좋아요, 스크랩(saved) 할 수 있습니다.
- 💬 글 상세 페이지에서 댓글, 대댓글을 작성할 수 있습니다.
- ❌ 과도한 비방글은 삭제됩니다.

## 멤버 구성

- 🙋🏻‍♂️ 조성윤 🔗 [github/jsy78](https://github.com/jsy78)
- 🙋‍♂️ 강동현 🔗 [github/kangdh208](https://github.com/kangdh208)
- 🙋🏻 임선주 🔗 [github/snnzzoo](https://github.com/snnzzoo)
- 🙋🏼‍♂️ 장성민 🔗 [github/min486](https://github.com/min486)

<hr>

## 프로젝트 결과

- 메인 & 후기쓰기

![맛팔해조_gif](README.assets/맛팔해조.gif)

- 상세페이지

![맛팔해조2](README.assets/맛팔해조2.gif)

- 마이페이지

![맛팔해조3](README.assets/맛팔해조3.gif)

## 화면 설계

🔗 [피그마 URL](https://www.figma.com/file/0CXots81SBA0JT6L88SfmP/%EB%A7%9B%ED%8C%94%ED%95%B4%EC%A1%B0?node-id=0%3A1)

## 프로젝트 로고

![맛팔해조_로고](README.assets/맛팔해조_로고.png)

## 프로젝트 구조

- main.html : 메인 페이지, 기본 홈 url
- detail.html : 글(후기)의 지도, 좋아요 & 스크랩 & 조회 수, 댓글 & 대댓글 가능
- form.html : 후기 작성, 수정, 삭제 페이지
- mypage.html : 작성한 글 / 작성한 댓글 / 좋아요한 글 / 스크랩한 글 / 팔로우한 유저 확인 페이지, 회원 정보 수정 가능

```
│  README.md
├── accounts
│    └── templates
│         ├── followings.html
│         ├── index.html
│         ├── login.html
│         ├── mypage.html
│         ├── password.html
│         ├── profile.html
│         ├── signup.html
│         └── update.html
├── articles
│    └── templates
│         ├── detail.html
│         ├── form.html
│         ├── index.html
│         └── saved.html
├── search
│    └── templates
│         └── search.html
├── pjt
│	 ├── settings.py
│    └── templates
│        └── search.html  
└── static
     ├── css
     │	  ├── style.css
     │	  └── style2.css
     └── js
     	  ├── address.css
     	  ├── comment.css
     	  ├── footer.css
     	  ├── heart.css
     	  ├── mapscript.css
     	  ├── mapsearch.css
     	  ├── scrap.css
    	  └── script.css
```

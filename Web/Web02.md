# WEB

## CSS 기본 스타일

### 크기 단위

- px

  - 모니터 해상도의 한 화소인 픽셀 기준
  - 픽셀의 크기는 변하지 않으므로 고정적인 단위

- %

  - 백분율 단위
  - 가변적인 레이아웃에서 자주 사용

- em

  - (바로 위, 부모 요소에 대한) 상속의 영향을 받음
  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐

- rem

  - (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
  - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐

- em vs rem

  | ![https://ibb.co/QvKbz4T](https://i.ibb.co/yFQfGrZ/1.png) | ![https://ibb.co/2kZWGHQ](https://i.ibb.co/bKbQcDZ/2.png) |
  | --------------------------------------------------------- | --------------------------------------------------------- |

  | ![https://ibb.co/wpfDfGK](https://i.ibb.co/RQqLqrC/3.png) |
  | :-------------------------------------------------------: |

- viewport

  - 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역 (디바이스 화면)
  - 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
  - vw, vh, vmin, vmax

  | ![https://ibb.co/n1pDGbh](https://i.ibb.co/hd0K6yp/4.png) | ![https://ibb.co/Tg0LW5x](https://i.ibb.co/MC16BLx/5.png) |
  | --------------------------------------------------------- | --------------------------------------------------------- |

### 색상 단위

- 색상 키워드(`background-color: red;`)
  - 대소문자를 구분하지 않음
  - red, blue, black 과 같은 특정 색을 직접 글자로 나타냄
- RGB 색상(`background-color: rgb(0, 255, 0);`)
  - 16진수 표기법(`#`) 혹은 함수형 표기법(`rgb()`)을 사용해서 특정 색을 표현하는 방식
- HSL 색상(`background-color: hsl(0, 100%, 50%);`)
  - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식
- a는 alpha(투명도)

![https://ibb.co/PwrpFZ6](https://i.ibb.co/dGf9j05/6.png)

### CSS 문서 표현

- 텍스트
  - 서체(`font-family`), 서체 스타일(`font-style`,` font-weight` 등)
  - 자간(`letter-spacing`), 단어 간격(`word-spacing`), 행간(`line-height`) 등
- 컬러(`color`), 배경(`background-image`, `background-color`)
- 기타 HTML 태그별 스타일링
  - 목록(`li`), 표(`table`)

## CSS Selectors

### 선택자 유형

- 기본 선택자
  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자
- 결합자(Combinators)
  - 자손 결합자, 자식 결합자
  - 일반 형제 결합자, 인접 형제 결합자
- 의사 클래스/요소(Pseudo Class)
  - 링크, 동적 의사 클래스
  - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

### 선택자 정리

- 요소 선택자
  - HTML 태그를 직접 선택
- 클래스 선택자
  - 마침표(.) 문자로 시작하며, 해당 클래스가 적용된 항목을 선택
- 아이디 선택자
  - \# 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
  - 일반적으로 하나의 문서에 1번만 사용
  - 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장

### 우선순위

![https://ibb.co/K5FvvgP](https://i.ibb.co/GdcSSD6/specificityimg.png)

1. 중요도 (Importance) : 만약 나중에 설정한 값이 적용되지 않게 하려면 속성값 뒤에 `!important`를 붙임

   ```css
   p {
     color: red !important;
   }
   p {
     color: blue;
   }
   /* 원래대로라면 글자색은 파란색이겠지만 red 뒤에 !important 글자색은 빨간색을 유지함 */
   /* 중요도는 사용할 때 반드시 주의할 것! */
   ```

2. 우선 순위 (Specificity)
   -  인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
3. CSS 파일 로딩 순서

### 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 물려줌
  - 속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있음
    - 상속 되는 것
      - Text 관련 요소(`font`, `color`, `text-align`), `opacity`, `visibility` 등
    - 상속 되지 않는 것 
      - Box model 관련 요소(`width`, `height`, `margin`, `padding`, `border`, `box-sizing`, `display`)
      - position 관련 요소(`position`, `top`/`right`/`bottom`/`left`,` z-index`)
      - 그 외 기타 등등
  - 상속 가능 여부는 MDN 문서에서 확인할 것

| ![https://ibb.co/HtzPGQs](https://i.ibb.co/R306QWm/7.png) | ![https://ibb.co/WcYqJ9B](https://i.ibb.co/7G68mcr/8.png) |
| --------------------------------------------------------- | --------------------------------------------------------- |

- 상속이 되지 않아서 span에는 border가 없음

  ![https://ibb.co/VCywnn2](https://i.ibb.co/kDnmbbQ/9.png)

- 상속이 되었다면 span에도 border가 적용되어야 함

  ![https://ibb.co/SPWZDmC](https://i.ibb.co/KXR8csv/10.png)

## CSS Box Model

![https://ibb.co/gTC71Rj](https://i.ibb.co/cFdv5rg/11.png)

### CSS 원칙 I

> 모든 요소는 네모(박스모델)이고, 
>
> 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다. 
>
> (좌측 상단에 배치)

![https://ibb.co/FYtxRXd](https://i.ibb.co/M1L2FfJ/12.png)

### Box model

- 모든 요소는 box 형태로 되어있음
- 하나의 박스는 네 부분(영역)으로 이루어짐
  - margin
  - border
  - padding
  - content

![https://ibb.co/KFMDg21](https://i.ibb.co/HnWCytJ/13.png)

```css
/* Box model 구성 (padding) */
.margin-padding {
    margin: 10px;
    padding: 30px;
}
```

![https://ibb.co/t8KG00F](https://i.ibb.co/0h2700v/14.png)

```css
/* Box model 구성 (margin/padding) */
.margin-1 {
    margin: 10px;
}
.margin-2 {
    margin: 10px 20px;
}
.margin-3 {
    margin: 10px 20px 30px;
}
.margin-4 {
    margin: 10px 20px 30px 40px;
}
/* 시계 방향 */
```

| ![https://ibb.co/9GcXzhF](https://i.ibb.co/b7QhqFS/15.png) |
| ---------------------------------------------------------- |
| ![https://ibb.co/pXcK29p](https://i.ibb.co/C0g9BTF/16.png) |

```css
/* Box model 구성 (border) */
.border {
    border-width: 2px;
    border-style: dashed;
    border-color: black;
}

.border {
    border: 2px dashed black;
}
/* 동일한 모양 */
```

![https://ibb.co/HVJ6zWy](https://i.ibb.co/PNSKh7y/17.png)

| ![https://ibb.co/Jj4bdYx](https://i.ibb.co/chHpvWb/18.png) | ![https://ibb.co/bHWfG9K](https://i.ibb.co/TKvCN3g/19.png) |
| ---------------------------------------------------------- | ---------------------------------------------------------- |

| ![https://ibb.co/WHxfJxv](https://i.ibb.co/wd04m0h/20.png) |
| :--------------------------------------------------------: |

#### box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box
  - border, padding을 제외한 순수 contents 영역만을 box로 지정
- 다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함
  - 그 경우 box-sizing을 border-box로 설정

![https://ibb.co/VqVqwp0](https://i.ibb.co/jrhrJZ9/21.png)

## CSS Display

### CSS 원칙 II

> - 모든 요소는 네모(박스모델)이고, 좌측상단에 배치.
> - display에 따라 크기와 배치가 달라진다.

### 대표적으로 활용되는 display

- `display: block`
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지함
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
- `display: inline`
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지함
  - `width`, `height`, `margin-top`, `margin-bottom`을 지정할 수 없음
  - 상하 여백은 `line-height`로 지정함

### 블록 레벨 요소 / 인라인 레벨 요소
| ![https://ibb.co/fGfpM6Y](https://i.ibb.co/x8Wjh9S/22.png) | ![https://ibb.co/sWXcnFw](https://i.ibb.co/5KJCm58/23.png) |
| ---------------------------------------------------------- | ---------------------------------------------------------- |
- 블록 레벨 요소와 인라인 레벨 요소 구분 (HTML 4.1까지)
- 대표적인 블록 레벨 요소 
  - `div` / `ul`, `ol`, `li` / `p` / `hr` / `form` 등
- 대표적인 인라인 레벨 요소
  - `span` / `a` / `img` / `input`, `label` / `b`, `em`, `i`, `strong` 등

#### block

![https://ibb.co/8N6Wy5t](https://i.ibb.co/zQGy3RD/24.png)

![https://ibb.co/GttjXgg](https://i.ibb.co/0FF3kPP/25.png)

- block의 기본 너비는 가질 수 있는 너비의 100%

![https://ibb.co/JzCGcZ3](https://i.ibb.co/jLHQ8tJ/26.png)

![https://ibb.co/HqZxCpv](https://i.ibb.co/jDtWzZK/27.png)

- 너비를 가질 수 없다면 자동으로 부여되는 `margin`

#### inline

![https://ibb.co/5njhWzv](https://i.ibb.co/WPzvWdF/28.png)

![https://ibb.co/Ybw0CsL](https://i.ibb.co/6NLXMCW/29.png)

- inline의 기본 너비는 content 영역만큼

### 속성에 따른 수평 정렬

![https://ibb.co/tXNVgV1](https://i.ibb.co/pysYcYk/30.png)

### 그 외 display

- `display: inline-block`
  - block과 inline 레벨 요소의 특징을 모두 가짐
  - inline처럼 한 줄에 표시할 수 있고, block처럼 `width`, `height`, `margin` 속성을 모두 지정할 수 있음
- `display: none`
  - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
  - 이와 비슷한 `visibility: hidden`은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않음

## 참고용 MDN 문서

- HTML : [https://developer.mozilla.org/ko/docs/Web/HTML](https://developer.mozilla.org/ko/docs/Web/HTML)

- CSS : [https://developer.mozilla.org/ko/docs/Web/CSS](https://developer.mozilla.org/ko/docs/Web/CSS)

- display : [https://developer.mozilla.org/ko/docs/Web/CSS/display](https://developer.mozilla.org/ko/docs/Web/CSS/display)
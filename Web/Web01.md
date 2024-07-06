# WEB

## 웹 사이트 기초

- [웹 사이트의 구성 요소](https://html-css-js.com/) : HTML (구조) + CSS (표현) + Javascript (동작)

- 웹 사이트는 브라우저를 통해 동작함

  - 브라우저마다 동작이 약간씩 달라서 문제가 생기는 경우가 많음 (파편화)

  - 해결책으로 웹 표준이 등장

    - 웹 표준 : 웹에서 표준으로 사용되는 기술이나 규칙, 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함 (크로스 브라우징)

- 웹 개발 도구 : Visual Studio Code, 크롬 개발자 도구

  - Visual Studio Code 추천 확장 프로그램
  
    - Open in browser 
  
    - Auto Rename Tag
  
    - Auto Close Tag
    
    - Intellisense for CSS class names in HTML
    
    - HTML CSS Support

  - 크롬 개발자 도구 주요 기능

    - Elements – DOM 탐색 및 CSS 확인 및 변경

    - Styles – 요소에 적용된 CSS 확인, 해당 요소에 선언된 모든 CSS

    - Computed – 스타일이 계산된 최종 결과, 해당 요소에 최종 계산된 CSS

    - Event Listeners – 해당 요소에 적용된 이벤트 (JS)

    - Sources, Network, Performance, Application, Security, Audits 등

## HTML 개념

- Hyper Text Markup Language : 웹 페이지를 작성(구조화)하기 위한 언어

  - Hyper Text : 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

  - Markup Language : 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

## HTML 기본 구조

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <!-- 이것은 주석입니다. -->
    <h1>나의 첫번째 HTML</h1>
    <p>이것은 본문입니다.</p>
    <span>이것은 인라인요소</span>
    <a href="https://www.naver.com">네이버로 이동!!</a>
</body>
</html>
```

- html : 문서의 최상위(root) 요소

- head : 문서 메타데이터 요소

  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등

  - 일반적으로 브라우저에 나타나지 않는 내용

- body : 문서 본문 요소

  - 실제 화면 구성과 관련된 내용

### head 

```html
<head>
    <title>HTML 수업</title>
    <meta charset="UTF-8">
    <link href="style.css" rel="stylesheet">
    <script src="javascript.js"></script>
    <style>
        p {
            color: black;
        } 
    </style>
</head>
```

- `<title>` : 브라우저 상단 타이틀

- `<meta>` : 문서 레벨 메타데이터 요소

- `<link>` : 외부 리소스 연결 요소 (CSS 파일, favicon 등)

- `<script>` : 스크립트 요소 (JavaScript 파일/코드)

- `<style>` : CSS 직접 작성

- Open Graph Protocol : 메타데이터를 표현하는 새로운 규약

  - HTML 문서의 메타데이터를 통해 문서의 정보를 전달

  - 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의

### element

> ```html
> <h1>contents</h1>
> ```
>
> HTML의 요소는 태그와 내용(contents)로 구성되어 있다.

- HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성

- 요소는 태그로 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의

- 내용이 없는 태그들도 존재(닫는 태그가 없음)

  - br, hr, img, input, link, meta

- 요소는 중첩(nested)될 수 있음

  - 요소의 중첩을 통해 하나의 문서를 구조화

  - 여는 태그와 닫는 태그의 쌍을 잘 확인해야 함

    - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어 질 수 있음

### attribute

> ```html
> <a href=“https://google.com”></a>
> ```
>
> 태그별로 사용할 수 있는 속성은 다르다.

- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음

- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공

- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재

- 태그와 상관없이 모든 HTML 요소가 공통으로 사용 가능한 속성(HTML Global Attribute)들도 있음

  - `id` : 문서 전체에서 유일한 고유 식별자 지정

  - `class` : 공백으로 구분된 해당 요소의 클래스의 목록 (CSS, JS에서 요소를 선택하거나 접근

  - `data-*` : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용

  - `style` : inline 스타일

  - `title` : 요소에 대한 추가 정보 지정

  - `tabindex` : 요소의 탭 순서

  - `dir` : 요소의 쓰기 방향

- 태그 간의 띄어쓰기, 엔터는 동작하지 않음

### Inline / Block

- HTML 요소는 크게 인라인 / 블록 요소로 나눔

- 인라인 요소는 글자처럼 취급

- 블록 요소는 한 줄 모두 사용

### Text

<img src="./img/1111.png" alt="./img/1111.png" style="zoom:67%;" />

| 태그                              | 설명                                                         |
| --------------------------------- | ------------------------------------------------------------ |
| `<a></a>`                         | href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성     |
| `<b></b>`<br/>`<strong></strong>` | 굵은 글씨 요소<br/>중요한 강조하고자 하는 요소 (보통 긁은 글씨로 표현) |
| `<i></i>`<br/>`<em></em>`         | 기울임 글씨 요소<br/>중요한 강조하고자 하는 요소 (보통 기울임 글씨로 표현) |
| `<br/>`                           | 텍스트 내에 줄 바꿈 생성                                     |
| `<img>`                           | src 속성을 활용하여 이미지 표현,<br/>alt 속성을 활용하여 대체 텍스트 |
| `<span></span>`                   | 의미 없는 인라인 컨테이너                                    |

### Group

<img src="./img/2222.png" alt="./img/2222.png" style="zoom:75%;" />

| 태그                               | 설명                                                         |
| ---------------------------------- | ------------------------------------------------------------ |
| `<p></p> `                         | 하나의 문단 (paragraph)                                      |
| `<hr>`                             | 문단 레벨 요소에서의 주제의 분리를 의미하며<br/>수평선으로 표현됨 (A Horizontal Rule) |
| `<ol></ol>`<br/>`<ul></ul>`        | 순서가 있는 리스트 (ordered)<br/>순서가 없는 리스트 (unordered) |
| `<pre></pre>`                      | HTML에 작성한 내용을 그대로 표현<br/>보통 고정폭 글꼴이 사용되고 공백문자를 유지 |
| `<code></code>`                    | 짧은 코드 조각을 나타내는 스타일                             | 
| `<blockquote>`<br/>`</blockquote>` | 텍스트가 긴 인용문<br/>주로 들여쓰기를 한 것으로 표현됨      |
| `<div></div>`                      | 의미 없는 블록 레벨 컨테이너                                 |

## DOM

<img src="./img/1200px-DOM-model.svg.png" alt="문서 객체 모델" style="zoom: 35%;" />

- Document Object Model Tree

- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조

  - 렌더링(Rendering) : 웹 사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정

  - HTML 문서에 대한 모델을 구성함

  - HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공함

## CSS 기초

> ```css
> h1 { /* 선택자 */
>     color: blue; /* 선언 */
>     font-size: 15px;
>    /* 속성 */ /* 값 */
> }
> ```
>
> 선택하고, 스타일을 지정한다.

- Cascading Style Sheets

- 스타일을 지정하기 위한 언어

- CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택

- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행

- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미

  - 속성 (Property) : 어떤 스타일 기능을 변경할지 결정

  - 값 (Value) : 어떻게 스타일 기능을 변경할지 결정

### CSS 정의

- 인라인

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
  </head>
  <body>
      <h1 style="color: blue; font-size: 100px;">Hello</h1> 
      <!-- 해당 태그에 직접 style 속성을 활용 -->
  </body>
  </html>
  ```

- 내부 참조

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <style>
          h1 {
              color: blue;
              font-size: 100px;
          }
      </style>
      <!-- <head> 태그 내에 <style>로 지정 -->
  </head>
  <body>
  </body>
  </html>
  ```

- 외부 참조
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <link rel="stylesheet" href="mystyle.css">
      <!-- 외부 CSS 파일을 <head> 내 <link>를 통해 불러오기 -->
  </head>
  <body>
  </body>
  </html>
  ```
  
  ```css
  /* mystyle.css */
  h1 {
      color: blue;
      font-size: 100px;
  }
  ```

### CSS 기초 선택자

- 요소 선택자

  - HTML 태그를 직접 선택

- 클래스(class) 선택자

  - 마침표(.)문자로 시작하며, 해당 클래스가 적용된 항목을 선택

- 아이디(id) 선택자

  - \# 문자로 시작하며, 해당 아이디가 적용된 항목을 선택

  - 일반적으로 하나의 문서에 한 번만 사용

  - 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장

  - id는 잘 활용하지 않고, 자바스크립트로 개발할 때 주로 활용

### CSS 적용 우선순위

- id > class > 태그 순으로 우선순위를 가짐

- 같은 레벨이라면 나중에 선언된 것이 적용됨

- 일반적으로 CSS 스타일링은 클래스로만 함

## 참고용 MDN 문서

- HTML : [https://developer.mozilla.org/ko/docs/Web/HTML](https://developer.mozilla.org/ko/docs/Web/HTML)

- CSS : [https://developer.mozilla.org/ko/docs/Web/CSS](https://developer.mozilla.org/ko/docs/Web/CSS)
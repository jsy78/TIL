# WEB

## table

- table의 각 영역을 명시하기 위해 `<thead>` `<tbody>` `<tfoot>` 요소를 활용

  ![https://ibb.co/Np4WnLP](https://i.ibb.co/d6hkJQq/1.png)
  
- `<tr>`로 가로 줄을 구성하고 내부에는 `<th>` 혹은 `<td>`로 셀을 구성  

  ![https://ibb.co/Qbxm72j](https://i.ibb.co/BzYsHXK/2.png)
  
- `colspan`, `rowspan` 속성을 활용하여 셀 병합

  ![https://ibb.co/vHVYGLp](https://i.ibb.co/W6GtwBZ/3.png)

- `<caption>`을 통해 표 설명 또는 제목을 나타냄

  ![https://ibb.co/yqHLrCs](https://i.ibb.co/BB089Js/4.png)

- table 태그 기본 구성

  - `thead`
    - `tr` → `th`

  - `tbody`
    - `tr` → `td`

  - `tfoot`
    - `tr` → `td`

  - `caption`
  
- table 코드

  ```html
  <body>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Major</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>홍길동</td>
          <td>Computer Science</td>
        </tr>
        <tr>
          <td>2</td>
          <td>김철수</td>
          <td>Business</td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <td>총계</td>
          <td colspan="2">2명</td>
        </tr>
      </tfoot>
      <caption>1반 학생 명단</caption>
    </table>
  </body>
  ```

## form

- `<form>`은 정보(데이터)를 서버에 제출하기 위해 사용하는 태그

- `<form>` 기본 속성
  - action : form을 처리할 서버의 URL(데이터를 보낼 곳)
  - method : form을 제출할 때 사용할 HTTP 메서드 (GET 혹은 POST)
  - enctype : method가 post인 경우 데이터의 유형
    - application/x-www-form-urlencoded : 기본값
    - multipart/form-data : 파일 전송시 (input type이 file인 경우)
    - text/plain : HTML5 디버깅 용 (잘 사용되지 않음)


| ![https://ibb.co/v4t5DRg](https://i.ibb.co/SwLTJGW/5.png) | ![https://ibb.co/C0nMnxv](https://i.ibb.co/Qm6C6sn/6.png) |
| --------------------------------------------------------- | --------------------------------------------------------- |

## input

- 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
- `<input>` 대표적인 속성
  - name : form control에 적용되는 이름 (이름/값 페어로 전송됨)
  - value : form control에 적용되는 값 (이름/값 페어로 전송됨)
  - required, readonly, autofocus, autocomplete, disabled 등


| ![https://ibb.co/kydj26m](https://i.ibb.co/YWrmBT0/7.png) | ![https://ibb.co/5Mgh162](https://i.ibb.co/VjcYLt3/8.png) |
| --------------------------------------------------------- | --------------------------------------------------------- |

### input label

- label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
  - 사용자는 선택할 수 있는 영역이 늘어나 웹 / 모바일(터치) 환경에서 편하게 사용할 수 있음
  - label과 input 입력의 관계가 시각적으로 표현됨
  - 화면 리더기에서 label을 읽어 쉽게 내용을 확인 할 수 있도록 함
- `<input>`에 id 속성을, `<label>`에는 for 속성을 활용하여 상호 연관을 시킴

```html
<label for="agreement">개인정보 수집에 동의합니다.</label>
<input id="agreement" type="checkbox" name="agreement">
```

```html
<body>
  <h1>Form 활용 실습</h1>
    <form action="">
      <!-- autofocus 및 label 확인 -->
      <div class="input-group">
        <label for="username">아이디</label>
      </div>
      <input type="text" name="username" id="username" autofocus>

      <!-- disabled 및 value 확인 -->
      <div class="input-group">
        <label for="name">이름</label>
      </div>
      <input type="text" name="name" value="홍길동" id="name" disabled>

      <!-- label 확인 -->
      <div class="input-group">
        <label for="agreement">개인정보 수집에 동의합니다.</label>
      </div>
      <input type="checkbox" name="agreement" id="agreement">
      <div class="input-group">
        <label>최종 제출을 확인합니다.</label>
      </div>
      <input type="checkbox">
    </form>
    <input type="submit" value="제출">
</body>
```

![https://ibb.co/YXHCdWQ](https://i.ibb.co/QkygHcQ/10.png)

### input - 일반

![https://ibb.co/58SKHKf](https://i.ibb.co/ncYPJP5/11.png)

- 일반적으로 입력을 받기 위하여 제공되며 타입별로 HTML기본 검증 혹은 추가 속성을 활용할 수 있음
  - text : 일반 텍스트 입력
  - password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
  - email : 이메일 형식이 아닌 경우 form 제출 불가
  - number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
  - file : accept 속성을 활용하여 파일 타입 지정 가능

### input - 선택

![https://ibb.co/41v5pVP](https://i.ibb.co/CPCTQHh/12.png)

- 일반적으로 label 태그와 함께 사용하여 선택 항목을 작성함
- 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 value를 지정해야 함
  - checkbox : 다중 선택
  - radio : 단일 선택

```html
<div>
  <p>checkbox</p>
  <input id="html" type="checkbox" name="language" value="html">
  <label for="html">HTML</label>
  <input id="python" type="checkbox" name="language" value="python">
  <label for="python">파이썬</label>
  <input id="java" type="checkbox" name="language" value="java">
  <label for="java">자바</label>
  <hr>
</div>
```

### input - 기타

![https://ibb.co/Pj6TNTf](https://i.ibb.co/ZXMHVHk/13.png)

- 다양한 종류의 input을 위한 picker를 제공
  - color : color picker
  - date : date picker
- hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
  - hidden : 사용자에게 보이지 않는 input

## Bootstrap

> ![https://ibb.co/z4ychvQ](https://i.ibb.co/nLH2sJ6/14.png)
>
> Bootstrap으로 빠른 반응형 사이트를 구축하십시오.
>
> Sass 변수 및 믹스인, **반응형 그리드 시스템**, **사전 구축된 광범위한 컴포넌트** 및 강력한 JavaScript 플러그인을 특징으로 하는
>
> **세계에서 가장 인기 있는** 프론트 엔드 오픈 소스 툴킷인 Bootstrap으로 **반응형** 모바일 우선 사이트를 **빠르게** 디자인하고 사용자 정의하십시오.

![https://ibb.co/x1pf9Vg](https://i.ibb.co/tq7xjy2/15.png)

![https://ibb.co/gZ7VZSF](https://i.ibb.co/d4cg4PJ/16.png)

### CDN

- Content Delivery(Distribution) Network

- 컨텐츠(CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드를 가진 네트워크에 데이터를 제공하는 시스템

- 개별 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점)

- 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐

- Bootstrap CDN

  ```html
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.min.js" integrity="sha384-ODmDIVzN+pFdexxHEHFBQH3/9/vQ9uori45z4JjnFsRydbmQbmL5t1tQ0culUzyK" crossorigin="anonymous"></script>
  ```

### spacing

```html
<div class="mt-3 ms-5">bootstrap-spacing</div>
```

![https://ibb.co/2Kvg6G8](https://i.ibb.co/dKPGc8b/17.png)

- Margin and padding
- {property}{sides}-{size}

  - Where *property* is one of

    - m : `margin`
    - p : `padding`

  - Where *sides* is one of
    - t : `margin-top` or `padding-top`
    - b : `margin-bottom` or` padding-bottom`
    - s : (start)
      - LTR (Left to Right) : `margin-left` or `padding-left`
      - RTL (Right to Left) : `margin-right` or `padding-right`
    - e : (end)
      - LTR (Left to Right) : `margin-right` or `padding-right`
      - RTL (Right to Left) : `margin-left` or `padding-left`
    - x : `*-left` and `*-right` (요소의 좌우 모두에 `margin` 또는 `padding` 설정)
    - y : `*-top` and `*-bottom` (요소의 상하 모두에 `margin` 또는 `padding` 설정)
    - blank : `*-top` and `*-bottom` and  `*-left` and `*-right` (요소의 상하좌우 모두에 margin 또는 padding 설정)
  - Where *size* is one of
    - 0 : 0으로 설정하여 `margin` 또는 `padding` 제거
    - 1 : (기본적으로) `margin` 또는 `padding`을 `$spacer` * 0.25로 설정
    - 2 : (기본적으로) `margin` 또는 `padding`을 `$spacer` * 0.5로 설정
    - 3 : (기본적으로) `margin` 또는 `padding`을 `$spacer` * 1로 설정
    - 4 : (기본적으로) `margin` 또는 `padding`을 `$spacer` * 1.5로 설정
    - 5 : (기본적으로) `margin` 또는 `padding`을 `$spacer` * 3로 설정
    - auto : `margin`을 자동으로 설정


```css
.mt-1 {
  margin-top: 0.25rem !important;
    /* 0.25rem ? */
}
```

![https://ibb.co/mNZ0Kvr](https://i.ibb.co/8Yvbwzn/18.png)

| class name | rem  |  px  |
| :--------: | :--: | :--: |
|    m-1     | 0.25 |  4   |
|    m-2     | 0.5  |  8   |
|    m-3     |  1   |  16  |
|    m-4     | 1.5  |  24  |
|    m-5     |  3   |  48  |

```css
.mx-0 {
  margin-right: 0 !important;
  margin-left: 0 !important;
}
/* 왼쪽, 오른쪽 margin이 0 */
```

```css
.mx-auto {
  margin-right: auto !important;
  margin-left: auto !important;
}
/* 블록 요소 수평 중앙 정렬 (가로 가운데 정렬)
```

```css
.py-0 {
  padding-top: 0 !important;
  padding-bottom: 0 !important;
}
/* 위, 아래 padding이 0 */
```

![https://ibb.co/wYr1qBh](https://i.ibb.co/vDv8WV4/19.png)

### breakpoints

- Bootstrap의 장치 또는 viewport 크기에서 반응형 레이아웃이 작동하는 방식을 결정하는 사용자 지정 가능한 너비

| Breakpoint       | Class infix | Dimensions |
| ---------------- | ----------- | ---------- |
| Extra small      | *None*      | < 576px    |
| Small            | `sm`        | ≥ 576px    |
| Medium           | `md`        | ≥ 768px    |
| Large            | `lg`        | ≥ 992px    |
| Extra large      | `xl`        | ≥ 1200px   |
| xtra extra large | `xxl`       | ≥ 1400px   |

### color

| ![https://ibb.co/gmPHCL6](https://i.ibb.co/jbWBFPH/20.png) | ![https://ibb.co/688sWTS](https://i.ibb.co/9hhYr10/21.png) |
| ---------------------------------------------------------- | ---------------------------------------------------------- |

```html
<h2>Color</h2>
<div class="bg-primary">이건 파랑</div>
<div class="bg-secondary">이건 회색</div>
<div class="bg-danger">이건 빨강</div>
<p class="text-success">이건 초록색 글씨</p>
<p class="text-danger">이건 빨간색 글씨</p>
```

![https://ibb.co/KyhKdH7](https://i.ibb.co/0J2sT3Z/23.png)

### text

```html
<h2>Text</h2>
<p class="text-start">margin-top 3</p>
<p class="text-center">margin 4</p>
<p class="text-end">mx-auto, 가운데 정렬</p>
<a href="#" class="text-decoration-none">Non-underlined link</a>
<p class="fw-bold">Bold text.</p>
<p class="fw-normal">Normal weight text.</p>
<p class="fw-light">Light weight text.</p>
<p class="fst-italic">Italic text.</p>
```

![https://ibb.co/MhzGxdN](https://i.ibb.co/QcWC30m/25.png)

### display

```html
<h2>Display</h2>
<div class="d-inline p-2 bg-primary text-white">d-inline</div>
<div class="d-inline p-2 bg-dark text-white">d-inline</div>
<div class="d-block p-2 bg-dark text-white">d-block</div>
<div class="d-block p-2 bg-primary text-white">d-block</div>
<div class="box bg-warning d-sm-none d-md-block">보이나?? 안보이나??</div>
<div class="box bg-success d-md-none d-xl-block">보이나?? 안보이나??</div>
```

![https://ibb.co/9NdGGwz](https://i.ibb.co/c1sxxbM/26.png)

| Screen size         | Class                             |
| ------------------- | --------------------------------- |
| Hidden on all       | `.d-none`                         |
| Hidden only on xs   | `.d-none .d-sm-block`             |
| Hidden only on sm   | `.d-sm-none .d-md-block`          |
| Hidden only on md   | `.d-md-none .d-lg-block`          |
| Hidden only on lg   | `.d-lg-none .d-xl-block`          |
| Hidden only on xl   | `.d-xl-none`                      |
| Hidden only on xxl  | `.d-xxl-none .d-xxl-block`        |
| Visible on all      | `.d-block`                        |
| Visible only on xs  | `.d-block .d-sm-none`             |
| Visible only on sm  | `.d-none .d-sm-block .d-md-none`  |
| Visible only on md  | `.d-none .d-md-block .d-lg-none`  |
| Visible only on lg  | `.d-none .d-lg-block .d-xl-none`  |
| Visible only on xl  | `.d-none .d-xl-block .d-xxl-none` |
| Visible only on xxl | `.d-none .d-xxl-block`            |

### position

```html
<h2>Position</h2>
<div class="box fixed-top">fixed-top</div>
<div class="box fixed-bottom">fixed-bottom</div>
```

![https://ibb.co/hfcwMgV](https://i.ibb.co/M6fQhg7/27.png)

```html
<div class="position-static">...</div>
<div class="position-relative">...</div>
<div class="position-absolute">...</div>
<div class="position-fixed">...</div>
<div class="position-sticky">...</div>
```

- {property}-{position}
  - Where *property* is one of:
    - `top` - for the vertical `top` position
    - `start` - for the horizontal `left` position (in LTR)
    - `bottom` - for the vertical `bottom` position
    - `end` - for the horizontal `right` position (in LTR)
  - Where *position* is one of:
    - `0` - for `0` edge position
    - `50` - for `50%` edge position
    - `100` - for `100%` edge position

## 참고용 문서

- form
  - https://developer.mozilla.org/ko/docs/Learn/Forms
  - https://web.dev/learn/forms/ 
- Bootstrap
  - [Get started with Bootstrap · Bootstrap v5.2 (getbootstrap.com)](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
  - https://getbootstrap.com/docs/5.2/layout/breakpoints/
  - https://getbootstrap.com/docs/5.2/content/
  - https://getbootstrap.com/docs/5.2/forms
  - https://getbootstrap.com/docs/5.2/utilities
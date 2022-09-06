# Web

## Bootstrap

### Utilities

#### Colors

![https://ibb.co/J3p8hKf](https://i.ibb.co/NTNf4s8/9.png)

```html
<p class="text-primary">.text-primary</p>
<p class="text-secondary">.text-secondary</p>
<p class="text-success">.text-success</p>
<p class="text-danger">.text-danger</p>
<p class="text-warning bg-dark">.text-warning</p>
<p class="text-info bg-dark">.text-info</p>
<p class="text-light bg-dark">.text-light</p>
<p class="text-dark">.text-dark</p>
<p class="text-body">.text-body</p>
<p class="text-muted">.text-muted</p>
<p class="text-white bg-dark">.text-white</p>
<p class="text-black-50">.text-black-50</p>
<p class="text-white-50 bg-dark">.text-white-50</p>
```

#### Flex

##### Enable flex behaviors

```html
<div class="d-flex p-2">I'm a flexbox container!</div>
```

```html
<div class="d-inline-flex p-2">I'm an inline flexbox container!</div>
```

- `.d-flex`
- `.d-inline-flex`
- `.d-sm-flex`
- `.d-sm-inline-flex`
- `.d-md-flex`
- `.d-md-inline-flex`
- `.d-lg-flex`
- `.d-lg-inline-flex`
- `.d-xl-flex`
- `.d-xl-inline-flex`
- `.d-xxl-flex`
- `.d-xxl-inline-flex`

##### Direction

```html
<div class="d-flex flex-row mb-3">
  <div class="p-2">Flex item 1</div>
  <div class="p-2">Flex item 2</div>
  <div class="p-2">Flex item 3</div>
</div>
<div class="d-flex flex-row-reverse">
  <div class="p-2">Flex item 1</div>
  <div class="p-2">Flex item 2</div>
  <div class="p-2">Flex item 3</div>
</div>
<div class="d-flex flex-column mb-3">
  <div class="p-2">Flex item 1</div>
  <div class="p-2">Flex item 2</div>
  <div class="p-2">Flex item 3</div>
</div>
<div class="d-flex flex-column-reverse">
  <div class="p-2">Flex item 1</div>
  <div class="p-2">Flex item 2</div>
  <div class="p-2">Flex item 3</div>
</div>
```

- `.flex-row`
- `.flex-row-reverse`
- `.flex-column`
- `.flex-column-reverse`
- `.flex-sm-row`
- `.flex-sm-row-reverse`
- `.flex-sm-column`
- `.flex-sm-column-reverse`
- `.flex-md-row`
- `.flex-md-row-reverse`
- `.flex-md-column`
- `.flex-md-column-reverse`
- `.flex-lg-row`
- `.flex-lg-row-reverse`
- `.flex-lg-column`
- `.flex-lg-column-reverse`
- `.flex-xl-row`
- `.flex-xl-row-reverse`
- `.flex-xl-column`
- `.flex-xl-column-reverse`
- `.flex-xxl-row`
- `.flex-xxl-row-reverse`
- `.flex-xxl-column`
- `.flex-xxl-column-reverse`

##### Justify content

```html
<div class="d-flex justify-content-start">...</div>
<div class="d-flex justify-content-end">...</div>
<div class="d-flex justify-content-center">...</div>
<div class="d-flex justify-content-between">...</div>
<div class="d-flex justify-content-around">...</div>
<div class="d-flex justify-content-evenly">...</div>
```

- `.justify-content-start`
- `.justify-content-end`
- `.justify-content-center`
- `.justify-content-between`
- `.justify-content-around`
- `.justify-content-evenly`
- `.justify-content-sm-start`
- `.justify-content-sm-end`
- `.justify-content-sm-center`
- `.justify-content-sm-between`
- `.justify-content-sm-around`
- `.justify-content-sm-evenly`
- `.justify-content-md-start`
- `.justify-content-md-end`
- `.justify-content-md-center`
- `.justify-content-md-between`
- `.justify-content-md-around`
- `.justify-content-md-evenly`
- `.justify-content-lg-start`
- `.justify-content-lg-end`
- `.justify-content-lg-center`
- `.justify-content-lg-between`
- `.justify-content-lg-around`
- `.justify-content-lg-evenly`
- `.justify-content-xl-start`
- `.justify-content-xl-end`
- `.justify-content-xl-center`
- `.justify-content-xl-between`
- `.justify-content-xl-around`
- `.justify-content-xl-evenly`
- `.justify-content-xxl-start`
- `.justify-content-xxl-end`
- `.justify-content-xxl-center`
- `.justify-content-xxl-between`
- `.justify-content-xxl-around`
- `.justify-content-xxl-evenly`

##### Align content

```html
<div class="d-flex align-content-start flex-wrap">...</div>
<div class="d-flex align-content-end flex-wrap">...</div>
<div class="d-flex align-content-center flex-wrap">...</div>
<div class="d-flex align-content-between flex-wrap">...</div>
<div class="d-flex align-content-around flex-wrap">...</div>
<div class="d-flex align-content-stretch flex-wrap">...</div>
<!-- flex item들이 단일 행에 위치해있을 경우 아무런 영향을 줄 수 없음 -->
```

- `.align-content-start`
- `.align-content-end`
- `.align-content-center`
- `.align-content-between`
- `.align-content-around`
- `.align-content-stretch`
- `.align-content-sm-start`
- `.align-content-sm-end`
- `.align-content-sm-center`
- `.align-content-sm-between`
- `.align-content-sm-around`
- `.align-content-sm-stretch`
- `.align-content-md-start`
- `.align-content-md-end`
- `.align-content-md-center`
- `.align-content-md-between`
- `.align-content-md-around`
- `.align-content-md-stretch`
- `.align-content-lg-start`
- `.align-content-lg-end`
- `.align-content-lg-center`
- `.align-content-lg-between`
- `.align-content-lg-around`
- `.align-content-lg-stretch`
- `.align-content-xl-start`
- `.align-content-xl-end`
- `.align-content-xl-center`
- `.align-content-xl-between`
- `.align-content-xl-around`
- `.align-content-xl-stretch`
- `.align-content-xxl-start`
- `.align-content-xxl-end`
- `.align-content-xxl-center`
- `.align-content-xxl-between`
- `.align-content-xxl-around`
- `.align-content-xxl-stretch`

##### Align items

```html
<div class="d-flex align-items-start">...</div>
<div class="d-flex align-items-end">...</div>
<div class="d-flex align-items-center">...</div>
<div class="d-flex align-items-baseline">...</div>
<div class="d-flex align-items-stretch">...</div>
```

- `.align-items-start`
- `.align-items-end`
- `.align-items-center`
- `.align-items-baseline`
- `.align-items-stretch`
- `.align-items-sm-start`
- `.align-items-sm-end`
- `.align-items-sm-center`
- `.align-items-sm-baseline`
- `.align-items-sm-stretch`
- `.align-items-md-start`
- `.align-items-md-end`
- `.align-items-md-center`
- `.align-items-md-baseline`
- `.align-items-md-stretch`
- `.align-items-lg-start`
- `.align-items-lg-end`
- `.align-items-lg-center`
- `.align-items-lg-baseline`
- `.align-items-lg-stretch`
- `.align-items-xl-start`
- `.align-items-xl-end`
- `.align-items-xl-center`
- `.align-items-xl-baseline`
- `.align-items-xl-stretch`
- `.align-items-xxl-start`
- `.align-items-xxl-end`
- `.align-items-xxl-center`
- `.align-items-xxl-baseline`
- `.align-items-xxl-stretch`

##### Align self

```html
<div class="align-self-start">Aligned flex item</div>
<div class="align-self-end">Aligned flex item</div>
<div class="align-self-center">Aligned flex item</div>
<div class="align-self-baseline">Aligned flex item</div>
<div class="align-self-stretch">Aligned flex item</div>
```

- `.align-self-start`
- `.align-self-end`
- `.align-self-center`
- `.align-self-baseline`
- `.align-self-stretch`
- `.align-self-sm-start`
- `.align-self-sm-end`
- `.align-self-sm-center`
- `.align-self-sm-baseline`
- `.align-self-sm-stretch`
- `.align-self-md-start`
- `.align-self-md-end`
- `.align-self-md-center`
- `.align-self-md-baseline`
- `.align-self-md-stretch`
- `.align-self-lg-start`
- `.align-self-lg-end`
- `.align-self-lg-center`
- `.align-self-lg-baseline`
- `.align-self-lg-stretch`
- `.align-self-xl-start`
- `.align-self-xl-end`
- `.align-self-xl-center`
- `.align-self-xl-baseline`
- `.align-self-xl-stretch`
- `.align-self-xxl-start`
- `.align-self-xxl-end`
- `.align-self-xxl-center`
- `.align-self-xxl-baseline`
- `.align-self-xxl-stretch`

##### Fill

![https://ibb.co/ZHpy9dW](https://i.ibb.co/dbwnZBG/1.png)

```html
<div class="d-flex">
  <div class="p-2 flex-fill">Flex item with a lot of content</div>
  <div class="p-2 flex-fill">Flex item</div>
  <div class="p-2 flex-fill">Flex item</div>
</div>
```

- `.flex-fill`
- `.flex-sm-fill`
- `.flex-md-fill`
- `.flex-lg-fill`
- `.flex-xl-fill`
- `.flex-xxl-fill`

##### Grow and Shrink

![https://ibb.co/3MfJdC5](https://i.ibb.co/qW0ZjrL/2.png)

```html
<div class="d-flex">
  <div class="p-2 flex-grow-1">Flex item</div>
  <div class="p-2">Flex item</div>
  <div class="p-2">Third flex item</div>
</div>
```

![https://ibb.co/7V0WLmn](https://i.ibb.co/bLGBD9s/3.png)

```html
<div class="d-flex">
  <div class="p-2 w-100">Flex item</div>
  <div class="p-2 flex-shrink-1">Flex item</div>
</div>
```

- `.flex-{grow|shrink}-0`
- `.flex-{grow|shrink}-1`
- `.flex-sm-{grow|shrink}-0`
- `.flex-sm-{grow|shrink}-1`
- `.flex-md-{grow|shrink}-0`
- `.flex-md-{grow|shrink}-1`
- `.flex-lg-{grow|shrink}-0`
- `.flex-lg-{grow|shrink}-1`
- `.flex-xl-{grow|shrink}-0`
- `.flex-xl-{grow|shrink}-1`
- `.flex-xxl-{grow|shrink}-0`
- `.flex-xxl-{grow|shrink}-1`

##### Auto margins

![https://ibb.co/wsq27d9](https://i.ibb.co/DpFjY1x/4.png)

```html
<div class="d-flex mb-3">
  <div class="p-2">Flex item</div>
  <div class="p-2">Flex item</div>
  <div class="p-2">Flex item</div>
</div>

<div class="d-flex mb-3">
  <div class="me-auto p-2">Flex item</div>
  <div class="p-2">Flex item</div>
  <div class="p-2">Flex item</div>
</div>

<div class="d-flex mb-3">
  <div class="p-2">Flex item</div>
  <div class="p-2">Flex item</div>
  <div class="ms-auto p-2">Flex item</div>
</div>
```

###### With align-items

![https://ibb.co/NYQXTYb](https://i.ibb.co/SvW2fvG/5.png)

```html
<div class="d-flex align-items-start flex-column mb-3" style="height: 200px;">
  <div class="mb-auto p-2">Flex item</div>
  <div class="p-2">Flex item</div>
  <div class="p-2">Flex item</div>
</div>

<div class="d-flex align-items-end flex-column mb-3" style="height: 200px;">
  <div class="p-2">Flex item</div>
  <div class="p-2">Flex item</div>
  <div class="mt-auto p-2">Flex item</div>
</div>
```

- by mixing `align-items`, `flex-direction: column`, and `margin-top: auto` or `margin-bottom: auto`

##### Wrap

```html
<div class="d-flex flex-nowrap">...</div>
<div class="d-flex flex-wrap">...</div>
<div class="d-flex flex-wrap-reverse">...</div>
```

- `.flex-nowrap`
- `.flex-wrap`
- `.flex-wrap-reverse`
- `.flex-sm-nowrap`
- `.flex-sm-wrap`
- `.flex-sm-wrap-reverse`
- `.flex-md-nowrap`
- `.flex-md-wrap`
- `.flex-md-wrap-reverse`
- `.flex-lg-nowrap`
- `.flex-lg-wrap`
- `.flex-lg-wrap-reverse`
- `.flex-xl-nowrap`
- `.flex-xl-wrap`
- `.flex-xl-wrap-reverse`
- `.flex-xxl-nowrap`
- `.flex-xxl-wrap`
- `.flex-xxl-wrap-reverse`

##### Order

![https://ibb.co/7bKw5rM](https://i.ibb.co/fQHh5r6/6.png)

```html
<div class="d-flex flex-nowrap">
  <div class="order-3 p-2">First flex item</div>
  <div class="order-2 p-2">Second flex item</div>
  <div class="order-1 p-2">Third flex item</div>
</div>
```

- `.order-0`
- `.order-1`
- `.order-2`
- `.order-3`
- `.order-4`
- `.order-5`
- `.order-sm-0`
- `.order-sm-1`
- `.order-sm-2`
- `.order-sm-3`
- `.order-sm-4`
- `.order-sm-5`
- `.order-md-0`
- `.order-md-1`
- `.order-md-2`
- `.order-md-3`
- `.order-md-4`
- `.order-md-5`
- `.order-lg-0`
- `.order-lg-1`
- `.order-lg-2`
- `.order-lg-3`
- `.order-lg-4`
- `.order-lg-5`
- `.order-xl-0`
- `.order-xl-1`
- `.order-xl-2`
- `.order-xl-3`
- `.order-xl-4`
- `.order-xl-5`
- `.order-xxl-0`
- `.order-xxl-1`
- `.order-xxl-2`
- `.order-xxl-3`
- `.order-xxl-4`
- `.order-xxl-5`
- `.order-first` : `order: -1`
- `.order-last` : `order: 6`
- `.order-sm-first`
- `.order-sm-last`
- `.order-md-first`
- `.order-md-last`
- `.order-lg-first`
- `.order-lg-last`
- `.order-xl-first`
- `.order-xl-last`
- `.order-xxl-first`
- `.order-xxl-last`

#### Position

##### Fixed

```html
<div class="fixed-top">...</div>
<div class="fixed-bottom">...</div>
```

##### Sticky

```html
<div class="sticky-top">...</div>
<div class="sticky-bottom">...</div>
```

###### Responsive sticky

```html
<div class="sticky-sm-top">Stick to the top on viewports sized SM (small) or wider</div>
<div class="sticky-md-top">Stick to the top on viewports sized MD (medium) or wider</div>
<div class="sticky-lg-top">Stick to the top on viewports sized LG (large) or wider</div>
<div class="sticky-xl-top">Stick to the top on viewports sized XL (extra-large) or wider</div>
<div class="sticky-xxl-top">Stick to the top on viewports sized XXL (extra-extra-large) or wider</div>
<div class="sticky-sm-bottom">Stick to the bottom on viewports sized SM (small) or wider</div>
<div class="sticky-md-bottom">Stick to the bottom on viewports sized MD (medium) or wider</div>
<div class="sticky-lg-bottom">Stick to the bottom on viewports sized LG (large) or wider</div>
<div class="sticky-xl-bottom">Stick to the bottom on viewports sized XL (extra-large) or wider</div>
<div class="sticky-xxl-bottom">Stick to the bottom on viewports sized XXL (extra-extra-large) or wider</div>
```

### Layout

#### Containers

```html
<div class="container">
  <!-- Content here -->
</div>

<div class="container-sm">100% wide until small breakpoint</div>
<div class="container-md">100% wide until medium breakpoint</div>
<div class="container-lg">100% wide until large breakpoint</div>
<div class="container-xl">100% wide until extra large breakpoint</div>
<div class="container-xxl">100% wide until extra extra large breakpoint</div>

<div class="container-fluid">
  <!-- Content here -->
</div>
```

- Bootstrap의 가장 기본적인 레이아웃 요소
- 기본 그리드 시스템을 사용할 때 필요함
- 컨텐츠을 포함하고 채우고 (때로는) 내용을 가운데에 맞추는 데 사용됨
- 중첩 가능하지만 대부분의 레이아웃에는 중첩 컨테이너가 필요하지 않음
- `.container` : 각 반응형 breakpoint에서 `max-width` 
- `.container-{breakpoint}` : 지정된 breakpoint까지 `width: 100%`
- `.container-fluid` : 모든 breakpoint에서`width: 100%`

|                    | Extra small<br/>< 576px | Small<br/>≥ 576px | Medium<br/>≥ 768px | Large<br/>≥ 992px | X-Large<br/>≥ 1200px | XX-Large<br/>≥ 1400px |
| ------------------ | :---------------------: | :---------------: | :----------------: | :---------------: | :------------------: | :-------------------: |
| `.container`       |          100%           |       540px       |       720px        |       960px       |        1140px        |        1320px         |
| `.container-sm`    |          100%           |       540px       |       720px        |       960px       |        1140px        |        1320px         |
| `.container-md`    |          100%           |       100%        |       720px        |       960px       |        1140px        |        1320px         |
| `.container-lg`    |          100%           |       100%        |        100%        |       960px       |        1140px        |        1320px         |
| `.container-xl`    |          100%           |       100%        |        100%        |       100%        |        1140px        |        1320px         |
| `.container-xxl`   |          100%           |       100%        |        100%        |       100%        |         100%         |        1320px         |
| `.container-fluid` |          100%           |       100%        |        100%        |       100%        |         100%         |         100%          |

### Content

#### Images

##### Responsive

```html
<img class="img-fluid" src="..." alt="...">
```

- `img-fluid` :  `max-width:100%` and `height:auto`

##### Thumbnails

```html
<img src="..." class="img-thumbnail" alt="...">
```

- 이미지에 둥근 1px 테두리 생성

##### Aligning

![https://ibb.co/87RZBg3](https://i.ibb.co/nLVJ0M2/7.png)

```html
<img src="..." class="rounded float-start" alt="...">
<img src="..." class="rounded float-end" alt="...">
```

![https://ibb.co/mS784mx](https://i.ibb.co/t35XDSd/8.png)

```html
<img src="..." class="rounded mx-auto d-block" alt="...">
```

```html
<div class="text-center">
  <img src="..." class="rounded" alt="...">
</div>
```

#### Typography

##### Heading

```html
<h1>h1. Bootstrap heading</h1>
<h2>h2. Bootstrap heading</h2>
<h3>h3. Bootstrap heading</h3>
<h4>h4. Bootstrap heading</h4>
<h5>h5. Bootstrap heading</h5>
<h6>h6. Bootstrap heading</h6>
```

```html
<h1 class="display-1">Display 1</h1>
<h1 class="display-2">Display 2</h1>
<h1 class="display-3">Display 3</h1>
<h1 class="display-4">Display 4</h1>
<h1 class="display-5">Display 5</h1>
<h1 class="display-6">Display 6</h1>
```

```css
$display-font-sizes: (
  1: 5rem,
  2: 4.5rem,
  3: 4rem,
  4: 3.5rem,
  5: 3rem,
  6: 2.5rem
);
```

##### List

###### Unstyled

![https://ibb.co/ZhSLSzF](https://i.ibb.co/vJhwh4T/10.png)

```html
<ul class="list-unstyled">
  <li>This is a list.</li>
  <li>It appears completely unstyled.</li>
  <li>Structurally, it's still a list.</li>
  <li>However, this style only applies to immediate child elements.</li>
  <li>Nested lists:
    <ul>
      <li>are unaffected by this style</li>
      <li>will still show a bullet</li>
      <li>and have appropriate left margin</li>
    </ul>
  </li>
  <li>This may still come in handy in some situations.</li>
</ul>
```

###### Inline

![https://ibb.co/JChjpMm](https://i.ibb.co/SJLwm95/11.png)

```html
<ul class="list-inline">
  <li class="list-inline-item">This is a list item.</li>
  <li class="list-inline-item">And another one.</li>
  <li class="list-inline-item">But they're displayed inline.</li>
</ul>
```

### Components

#### Accordion

- 아코디언은 접을 수 있도록 내부적으로 collapse를 사용
- 확장된 아코디언을 렌더링하려면 `.accordion`에 `.open` 클래스 추가
- id가 있는 경우 무조건 id를 일치시켜서 유지해야 함
  - 대부분 자바스크립트를 활용하고 있고, 타겟으로 활용되는 경우가 있음

##### Default

```html
<div class="accordion" id="accordionExample">
  <div class="accordion-item">
    <h2 class="accordion-header" id="headingOne">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
        Accordion Item #1
      </button>
    </h2>
    <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
      <div class="accordion-body">
        ...
      </div>
    </div>
  </div>
  <div class="accordion-item">
    <h2 class="accordion-header" id="headingTwo">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
        Accordion Item #2
      </button>
    </h2>
    <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
      <div class="accordion-body">
        ...
      </div>
    </div>
  </div>
  <div class="accordion-item">
    <h2 class="accordion-header" id="headingThree">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
        Accordion Item #3
      </button>
    </h2>
    <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#accordionExample">
      <div class="accordion-body">
        ...
      </div>
    </div>
  </div>
</div>
```

##### Flush

```html
<div class="accordion accordion-flush" id="accordionFlushExample">
  <div class="accordion-item">
    <h2 class="accordion-header" id="flush-headingOne">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
        Accordion Item #1
      </button>
    </h2>
    <div id="flush-collapseOne" class="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#accordionFlushExample">
      <div class="accordion-body">...</div>
    </div>
  </div>
  <div class="accordion-item">
    <h2 class="accordion-header" id="flush-headingTwo">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseTwo" aria-expanded="false" aria-controls="flush-collapseTwo">
        Accordion Item #2
      </button>
    </h2>
    <div id="flush-collapseTwo" class="accordion-collapse collapse" aria-labelledby="flush-headingTwo" data-bs-parent="#accordionFlushExample">
      <div class="accordion-body">...</div>
    </div>
  </div>
  <div class="accordion-item">
    <h2 class="accordion-header" id="flush-headingThree">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseThree" aria-expanded="false" aria-controls="flush-collapseThree">
        Accordion Item #3
      </button>
    </h2>
    <div id="flush-collapseThree" class="accordion-collapse collapse" aria-labelledby="flush-headingThree" data-bs-parent="#accordionFlushExample">
      <div class="accordion-body">...</div>
    </div>
  </div>
</div>
```

- `.accordion-flush` 클래스 추가

##### Always open

```html
<div class="accordion" id="accordionPanelsStayOpenExample">
  <div class="accordion-item">
    <h2 class="accordion-header" id="panelsStayOpen-headingOne">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseOne" aria-expanded="true" aria-controls="panelsStayOpen-collapseOne">
        Accordion Item #1
      </button>
    </h2>
    <div id="panelsStayOpen-collapseOne" class="accordion-collapse collapse show" aria-labelledby="panelsStayOpen-headingOne">
      <div class="accordion-body">
        ...
      </div>
    </div>
  </div>
  <div class="accordion-item">
    <h2 class="accordion-header" id="panelsStayOpen-headingTwo">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseTwo" aria-expanded="false" aria-controls="panelsStayOpen-collapseTwo">
        Accordion Item #2
      </button>
    </h2>
    <div id="panelsStayOpen-collapseTwo" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-headingTwo">
      <div class="accordion-body">
        ...
      </div>
    </div>
  </div>
  <div class="accordion-item">
    <h2 class="accordion-header" id="panelsStayOpen-headingThree">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-collapseThree" aria-expanded="false" aria-controls="panelsStayOpen-collapseThree">
        Accordion Item #3
      </button>
    </h2>
    <div id="panelsStayOpen-collapseThree" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-headingThree">
      <div class="accordion-body">
        ...
      </div>
    </div>
  </div>
</div>
```

- 각 `.accordion-collapse`에서 `data-bs-parent` 속성을 생략하면 다른 항목이 열릴 때 아코디언 항목이 열린 상태로 유지됨

#### Alerts

![https://ibb.co/sRcDRwQ](https://i.ibb.co/8sGRs52/12.png)

```html
<div class="alert alert-primary" role="alert">
  A simple primary alert—check it out!
</div>
<div class="alert alert-secondary" role="alert">
  A simple secondary alert—check it out!
</div>
<div class="alert alert-success" role="alert">
  A simple success alert—check it out!
</div>
<div class="alert alert-danger" role="alert">
  A simple danger alert—check it out!
</div>
<div class="alert alert-warning" role="alert">
  A simple warning alert—check it out!
</div>
<div class="alert alert-info" role="alert">
  A simple info alert—check it out!
</div>
<div class="alert alert-light" role="alert">
  A simple light alert—check it out!
</div>
<div class="alert alert-dark" role="alert">
  A simple dark alert—check it out!
</div>
```

![https://ibb.co/8bcvxWH](https://i.ibb.co/tzXj279/13.png)

```html
<div class="alert alert-primary d-flex align-items-center" role="alert">
  <svg xmlns="http://www.w3.org/2000/svg" class="bi bi-exclamation-triangle-fill flex-shrink-0 me-2" viewBox="0 0 16 16" role="img" aria-label="Warning:">
    <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
  </svg>
  <div>
    An example alert with an icon
  </div>
</div>
```

#### badge

![https://ibb.co/bH3xRYH](https://i.ibb.co/7gzHNBg/14.png)

```html
<h1>Example heading <span class="badge bg-secondary">New</span></h1>
<h2>Example heading <span class="badge bg-secondary">New</span></h2>
<h3>Example heading <span class="badge bg-secondary">New</span></h3>
<h4>Example heading <span class="badge bg-secondary">New</span></h4>
<h5>Example heading <span class="badge bg-secondary">New</span></h5>
<h6>Example heading <span class="badge bg-secondary">New</span></h6>
```

![https://ibb.co/z7dBmTD](https://i.ibb.co/mXp2RVg/15.png)

```html
<button type="button" class="btn btn-primary">
  Notifications <span class="badge text-bg-secondary">4</span>
</button>
```

![https://ibb.co/J7q7Qtm](https://i.ibb.co/tszsXKQ/16.png)

```html
<button type="button" class="btn btn-primary position-relative">
  Inbox
  <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
    99+
    <span class="visually-hidden">unread messages</span>
  </span>
</button>
```

#### Breadcrumb

![https://ibb.co/XWB4rQN](https://i.ibb.co/9pXvkDz/17.png)

```html
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item active" aria-current="page">Home</li>
  </ol>
</nav>

<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="#">Home</a></li>
    <li class="breadcrumb-item active" aria-current="page">Library</li>
  </ol>
</nav>

<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="#">Home</a></li>
    <li class="breadcrumb-item"><a href="#">Library</a></li>
    <li class="breadcrumb-item active" aria-current="page">Data</li>
  </ol>
</nav>
```

![https://ibb.co/jGB3HRQ](https://i.ibb.co/rMT5vsz/18.png)

```html
<nav style="--bs-breadcrumb-divider: '>';" aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="#">Home</a></li>
    <li class="breadcrumb-item active" aria-current="page">Library</li>
  </ol>
</nav>
```

#### Button

##### Basic

![https://ibb.co/RHcbXTL](https://i.ibb.co/pXdwHjC/19.png)

```html
<button type="button" class="btn btn-primary">Primary</button>
<button type="button" class="btn btn-secondary">Secondary</button>
<button type="button" class="btn btn-success">Success</button>
<button type="button" class="btn btn-danger">Danger</button>
<button type="button" class="btn btn-warning">Warning</button>
<button type="button" class="btn btn-info">Info</button>
<button type="button" class="btn btn-light">Light</button>
<button type="button" class="btn btn-dark">Dark</button>
<button type="button" class="btn btn-link">Link</button>
```

- `.btn-outline-*`
- `.btn-lg`
- `.btn-sm`

##### Disabled

![https://ibb.co/T8zwkYQ](https://i.ibb.co/4TBF7Kb/20.png)

```html
<button type="button" class="btn btn-primary" disabled>Primary button</button>
<button type="button" class="btn btn-secondary" disabled>Button</button>
<button type="button" class="btn btn-outline-primary" disabled>Primary button</button>
<button type="button" class="btn btn-outline-secondary" disabled>Button</button>
```

##### Close

```html
<button type="button" class="btn-close" aria-label="Close"></button>
```

```html
<button type="button" class="btn-close" disabled aria-label="Close"></button>
```

##### Toggle states 

```html
<button type="button" class="btn btn-primary" data-bs-toggle="button">Toggle button</button>
<button type="button" class="btn btn-primary active" data-bs-toggle="button" aria-pressed="true">Active toggle button</button>
<button type="button" class="btn btn-primary" disabled data-bs-toggle="button">Disabled toggle button</button>
```

```html
<a href="#" class="btn btn-primary" role="button" data-bs-toggle="button">Toggle link</a>
<a href="#" class="btn btn-primary active" role="button" data-bs-toggle="button" aria-pressed="true">Active toggle link</a>
<a class="btn btn-primary disabled" aria-disabled="true" role="button" data-bs-toggle="button">Disabled toggle link</a>
```

##### Methods

```js
const bsButton = new bootstrap.Button('#myButton')
```

| Method                | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| `dispose`             | 요소의 버튼 제거 (DOM 요소에 저장된 데이터 제거)             |
| `getInstance`         | DOM 요소에 연결된 버튼 인스턴스를 가져올 수 있는 정적 메소드는 다음과 같이 사용 가능 : <br/> `bootstrap.Button.getInstance(element)` |
| `getOrCreateInstance` | DOM 요소에 연결된 버튼 인스턴스를 반환하거나 초기화되지 않은 경우 새로 생성하는 정적 메소드 : <br/>`bootstrap.Button.getOrCreateInstance(element)` |
| `toggle`              | 버튼 클릭 여부 상태를 토글(전환), 버튼에 활성화된 모양 제공  |

```js
document.querySelectorAll('.btn').forEach(buttonElement => {
  const button = bootstrap.Button.getOrCreateInstance(buttonElement)
  button.toggle()
})
```

#### Button group

##### Basic

```html
<div class="btn-group" role="group" aria-label="Basic example">
  <button type="button" class="btn btn-primary">Left</button>
  <button type="button" class="btn btn-primary">Middle</button>
  <button type="button" class="btn btn-primary">Right</button>
</div>
```

```html
<div class="btn-group">
  <a href="#" class="btn btn-primary active" aria-current="page">Active link</a>
  <a href="#" class="btn btn-primary">Link</a>
  <a href="#" class="btn btn-primary">Link</a>
</div>
```

##### Outlined styles

```html
<div class="btn-group" role="group" aria-label="Basic outlined example">
  <button type="button" class="btn btn-outline-primary">Left</button>
  <button type="button" class="btn btn-outline-primary">Middle</button>
  <button type="button" class="btn btn-outline-primary">Right</button>
</div>
```

##### Checkbox and Radio

```html
<div class="btn-group" role="group" aria-label="Basic checkbox toggle button group">
  <input type="checkbox" class="btn-check" id="btncheck1" autocomplete="off">
  <label class="btn btn-outline-primary" for="btncheck1">Checkbox 1</label>

  <input type="checkbox" class="btn-check" id="btncheck2" autocomplete="off">
  <label class="btn btn-outline-primary" for="btncheck2">Checkbox 2</label>

  <input type="checkbox" class="btn-check" id="btncheck3" autocomplete="off">
  <label class="btn btn-outline-primary" for="btncheck3">Checkbox 3</label>
</div>
```

```html
<div class="btn-group" role="group" aria-label="Basic radio toggle button group">
  <input type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked>
  <label class="btn btn-outline-primary" for="btnradio1">Radio 1</label>

  <input type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
  <label class="btn btn-outline-primary" for="btnradio2">Radio 2</label>

  <input type="radio" class="btn-check" name="btnradio" id="btnradio3" autocomplete="off">
  <label class="btn btn-outline-primary" for="btnradio3">Radio 3</label>
</div>
```

##### Toolbar

```html
<div class="btn-toolbar" role="toolbar" aria-label="Toolbar with button groups">
  <div class="btn-group me-2" role="group" aria-label="First group">
    <button type="button" class="btn btn-primary">1</button>
    <button type="button" class="btn btn-primary">2</button>
    <button type="button" class="btn btn-primary">3</button>
    <button type="button" class="btn btn-primary">4</button>
  </div>
  <div class="btn-group me-2" role="group" aria-label="Second group">
    <button type="button" class="btn btn-secondary">5</button>
    <button type="button" class="btn btn-secondary">6</button>
    <button type="button" class="btn btn-secondary">7</button>
  </div>
  <div class="btn-group" role="group" aria-label="Third group">
    <button type="button" class="btn btn-info">8</button>
  </div>
</div>
```

##### Nesting

```html
<div class="btn-group" role="group" aria-label="Button group with nested dropdown">
  <button type="button" class="btn btn-primary">1</button>
  <button type="button" class="btn btn-primary">2</button>

  <div class="btn-group" role="group">
    <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
      Dropdown
    </button>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="#">Dropdown link</a></li>
      <li><a class="dropdown-item" href="#">Dropdown link</a></li>
    </ul>
  </div>
</div>
```

##### Vertical

```html
<div class="btn-group-vertical" role="group" aria-label="Vertical button group">
  <button type="button" class="btn btn-dark">Button</button>
  <button type="button" class="btn btn-dark">Button</button>
  <button type="button" class="btn btn-dark">Button</button>
  <button type="button" class="btn btn-dark">Button</button>
  <button type="button" class="btn btn-dark">Button</button>
  <button type="button" class="btn btn-dark">Button</button>
</div>
```

#### Card

```html
<!-- inline style이 있는 것을 반드시 확인할 것 -->
<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
```

```html
<div class="card" style="width: 18rem;">
  <div class="card-header">
    Featured
  </div>
  <ul class="list-group list-group-flush">
    <li class="list-group-item">An item</li>
    <li class="list-group-item">A second item</li>
    <li class="list-group-item">A third item</li>
  </ul>
</div>

<div class="card" style="width: 18rem;">
  <ul class="list-group list-group-flush">
    <li class="list-group-item">An item</li>
    <li class="list-group-item">A second item</li>
    <li class="list-group-item">A third item</li>
  </ul>
  <div class="card-footer">
    Card footer
  </div>
</div>
```

```html
<div class="card text-center">
  <div class="card-header">
    <ul class="nav nav-tabs card-header-tabs">
      <li class="nav-item">
        <a class="nav-link active" aria-current="true" href="#">Active</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled">Disabled</a>
      </li>
    </ul>
  </div>
  <div class="card-body">
    <h5 class="card-title">Special title treatment</h5>
    <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
```

#### Carousel

##### Controls

```html
<div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="..." class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="..." class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="..." class="d-block w-100" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
```

##### Indicators

```html
<div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="true">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="..." class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="..." class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="..." class="d-block w-100" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
```

##### Crossfade

```html
<div id="carouselExampleFade" class="carousel slide carousel-fade" data-bs-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="..." class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="..." class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="..." class="d-block w-100" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
```

#### Collapse

- Collapse JavaScript 플러그인은 컨텐츠를 표시하고 숨기는 데 사용됨
- 요소를 Collapsing하면 높이가 현재 값에서 0으로 애니메이션됨
- `.collapse` 요소에 `padding`을 사용할 수 없음
  - 대신 클래스를 독립적인 래핑 요소로 사용해야 함
- Accordion과 마찬가지로 무조건 id를 일치시켜서 유지해야 함
- `.collapse`은 컨텐츠를 숨김
- `.collapsing`은 전환 도중에 적용됨
- `.collapse.show`는 컨텐츠를 표시함

##### Vertical

```html
<p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">
    Link with href
  </a>
  <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
    Button with data-bs-target
  </button>
</p>
<div class="collapse" id="collapseExample">
  <div class="card card-body">
    Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
  </div>
</div>
```

##### Horizontal

```html
<p>
  <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseWidthExample" aria-expanded="false" aria-controls="collapseWidthExample">
    Toggle width collapse
  </button>
</p>
<div style="min-height: 120px;">
  <div class="collapse collapse-horizontal" id="collapseWidthExample">
    <div class="card card-body" style="width: 300px;">
      This is some placeholder content for a horizontal collapse. It's hidden by default and shown when triggered.
    </div>
  </div>
</div>
```

##### Multiple targets 

```html
<p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#multiCollapseExample1" role="button" aria-expanded="false" aria-controls="multiCollapseExample1">Toggle first element</a>
  <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#multiCollapseExample2" aria-expanded="false" aria-controls="multiCollapseExample2">Toggle second element</button>
  <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target=".multi-collapse" aria-expanded="false" aria-controls="multiCollapseExample1 multiCollapseExample2">Toggle both elements</button>
</p>
<div class="row">
  <div class="col">
    <div class="collapse multi-collapse" id="multiCollapseExample1">
      <div class="card card-body">
        Some placeholder content for the first collapse component of this multi-collapse example. This panel is hidden by default but revealed when the user activates the relevant trigger.
      </div>
    </div>
  </div>
  <div class="col">
    <div class="collapse multi-collapse" id="multiCollapseExample2">
      <div class="card card-body">
        Some placeholder content for the second collapse component of this multi-collapse example. This panel is hidden by default but revealed when the user activates the relevant trigger.
      </div>
    </div>
  </div>
</div>
```

#### Dropdown

```html
<div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
    Dropdown button
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
  </ul>
</div>
```

```html
<div class="dropdown">
  <a class="btn btn-secondary dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
    Dropdown link
  </a>

  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
  </ul>
</div>
```

##### Centered

```html
<div class="dropdown-center">
  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
    Centered dropdown
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Action two</a></li>
    <li><a class="dropdown-item" href="#">Action three</a></li>
  </ul>
</div>
```

##### Dropup

```html
<!-- Default dropup button -->
<div class="btn-group dropup">
  <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
    Dropup
  </button>
  <ul class="dropdown-menu">
    <!-- Dropdown menu links -->
  </ul>
</div>

<!-- Split dropup button -->
<div class="btn-group dropup">
  <button type="button" class="btn btn-secondary">
    Split dropup
  </button>
  <button type="button" class="btn btn-secondary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
    <span class="visually-hidden">Toggle Dropdown</span>
  </button>
  <ul class="dropdown-menu">
    <!-- Dropdown menu links -->
  </ul>
</div>
```

##### Dropup centered

```html
<div class="dropup-center dropup">
  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
    Centered dropup
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Action two</a></li>
    <li><a class="dropdown-item" href="#">Action three</a></li>
  </ul>
</div>
```

##### Dropend

```html
<!-- Default dropend button -->
<div class="btn-group dropend">
  <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
    Dropend
  </button>
  <ul class="dropdown-menu">
    <!-- Dropdown menu links -->
  </ul>
</div>

<!-- Split dropend button -->
<div class="btn-group dropend">
  <button type="button" class="btn btn-secondary">
    Split dropend
  </button>
  <button type="button" class="btn btn-secondary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
    <span class="visually-hidden">Toggle Dropend</span>
  </button>
  <ul class="dropdown-menu">
    <!-- Dropdown menu links -->
  </ul>
</div>
```

##### Dropstart

```html
<!-- Default dropstart button -->
<div class="btn-group dropstart">
  <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
    Dropstart
  </button>
  <ul class="dropdown-menu">
    <!-- Dropdown menu links -->
  </ul>
</div>

<!-- Split dropstart button -->
<div class="btn-group dropstart">
  <button type="button" class="btn btn-secondary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
    <span class="visually-hidden">Toggle Dropstart</span>
  </button>
  <ul class="dropdown-menu">
    <!-- Dropdown menu links -->
  </ul>
  <button type="button" class="btn btn-secondary">
    Split dropstart
  </button>
</div>
```

#### List group

```html
<ul class="list-group">
  <li class="list-group-item active" aria-current="true">An active item</li>
  <li class="list-group-item">A second item</li>
  <li class="list-group-item">A third item</li>
  <li class="list-group-item">A fourth item</li>
  <li class="list-group-item disabled" aria-disabled="true">A disabled item</li>
</ul>
```

```html
<ol class="list-group list-group-numbered">
  <li class="list-group-item">A list item</li>
  <li class="list-group-item">A list item</li>
  <li class="list-group-item">A list item</li>
</ol>
```

```html
<ul class="list-group list-group-horizontal">
  <li class="list-group-item">An item</li>
  <li class="list-group-item">A second item</li>
  <li class="list-group-item">A third item</li>
</ul>
```

#### Modal

- 라이트박스, 사용자 알림 또는 완전히 사용자 정의된 콘텐츠에 대한 다이얼로그를 사이트에 추가
- `position: fixed` 사용

```html
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
  Launch demo modal
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
```

#### Navbar

- `.navbar-expand{-sm|-md|-lg|-xl|-xxl}` : viewport 너비가 설정한 breakpoint보다 커지면 확장
- `.navbar-brand` : 회사, 제품,프로젝트 이름 또는 로고
- `.navbar-nav` : full-height and lightweight navigation (드롭다운 지원)
- `.navbar-toggler` : collapse plugin 및 기타 [navigation toggling](https://getbootstrap.com/docs/5.2/components/navbar/#responsive-behaviors) 동작과 함께 사용
- 모든 form 제어와 action을 위한 Flex 및 spacing 유틸리티
- `.navbar-text` : 세로 중앙에 텍스트 문자열 추가
- `.collapse.navbar-collapse` : 상위 breakpoint로 navbar contents를 그룹화하고 숨김 
- Add an optional `.navbar-scroll` to set a `max-height` and [scroll expanded navbar content](https://getbootstrap.com/docs/5.2/components/navbar/#scrolling)

```html
<nav class="navbar navbar-expand-lg bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled">Disabled</a>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
```

```html
<nav class="navbar navbar-expand-lg bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pricing</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled">Disabled</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```

```html
<nav class="navbar navbar-expand-lg bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <a class="nav-link active" aria-current="page" href="#">Home</a>
        <a class="nav-link" href="#">Features</a>
        <a class="nav-link" href="#">Pricing</a>
        <a class="nav-link disabled">Disabled</a>
      </div>
    </div>
  </div>
</nav>
```

#### Navs & Tabs

```html
<ul class="nav">
  <li class="nav-item">
    <a class="nav-link active" aria-current="page" href="#">Active</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link disabled">Disabled</a>
  </li>
</ul>
```

```html
<nav class="nav">
  <a class="nav-link active" aria-current="page" href="#">Active</a>
  <a class="nav-link" href="#">Link</a>
  <a class="nav-link" href="#">Link</a>
  <a class="nav-link disabled">Disabled</a>
</nav>
```

##### Horizontal alignment

```html
<ul class="nav justify-content-center">
  <li class="nav-item">
    <a class="nav-link active" aria-current="page" href="#">Active</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link disabled">Disabled</a>
  </li>
</ul>
```

```html
<ul class="nav justify-content-end">
  <li class="nav-item">
    <a class="nav-link active" aria-current="page" href="#">Active</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link disabled">Disabled</a>
  </li>
</ul>
```

##### Vertical

```html
<ul class="nav flex-column">
  <li class="nav-item">
    <a class="nav-link active" aria-current="page" href="#">Active</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link disabled">Disabled</a>
  </li>
</ul>
```

```html
<nav class="nav flex-column">
  <a class="nav-link active" aria-current="page" href="#">Active</a>
  <a class="nav-link" href="#">Link</a>
  <a class="nav-link" href="#">Link</a>
  <a class="nav-link disabled">Disabled</a>
</nav>
```

##### Tabs

```html
<ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link active" aria-current="page" href="#">Active</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link disabled">Disabled</a>
  </li>
</ul>
```

##### Tabs with dropdowns

```html
<ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link active" aria-current="page" href="#">Active</a>
  </li>
  <li class="nav-item dropdown">
    <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">Dropdown</a>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="#">Action</a></li>
      <li><a class="dropdown-item" href="#">Another action</a></li>
      <li><a class="dropdown-item" href="#">Something else here</a></li>
      <li><hr class="dropdown-divider"></li>
      <li><a class="dropdown-item" href="#">Separated link</a></li>
    </ul>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link disabled">Disabled</a>
  </li>
</ul>
```

#### Pagination

![https://ibb.co/VTCmDWB](https://i.ibb.co/x6gHGS5/21.png)

```html
<nav aria-label="Page navigation example">
  <ul class="pagination">
    <li class="page-item"><a class="page-link" href="#">Previous</a></li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item"><a class="page-link" href="#">Next</a></li>
  </ul>
</nav>
```

![https://ibb.co/khtQvcp](https://i.ibb.co/XzqSMJ9/22.png)

```html
<nav aria-label="...">
  <ul class="pagination">
    <li class="page-item disabled">
      <a class="page-link">Previous</a>
    </li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item active" aria-current="page">
      <a class="page-link" href="#">2</a>
    </li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item">
      <a class="page-link" href="#">Next</a>
    </li>
  </ul>
</nav>
```

#### Placeholders

- 아직 로딩 중임을 나타내는 컴포넌트

![https://ibb.co/jTKBVdV](https://i.ibb.co/nb2Z3T3/23.png)

```html
<div class="card">
  <img src="..." class="card-img-top" alt="...">

  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>

<div class="card" aria-hidden="true">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title placeholder-glow">
      <span class="placeholder col-6"></span>
    </h5>
    <p class="card-text placeholder-glow">
      <span class="placeholder col-7"></span>
      <span class="placeholder col-4"></span>
      <span class="placeholder col-4"></span>
      <span class="placeholder col-6"></span>
      <span class="placeholder col-8"></span>
    </p>
    <a href="#" tabindex="-1" class="btn btn-primary disabled placeholder col-6"></a>
  </div>
</div>
```

![https://ibb.co/QH6DjD0](https://i.ibb.co/s1FWJW7/24.png)

```html
<span class="placeholder col-6"></span>
<span class="placeholder w-75"></span>
<span class="placeholder" style="width: 25%;"></span>
```

##### Animation

```html
<p class="placeholder-glow">
  <span class="placeholder col-12"></span>
</p>

<p class="placeholder-wave">
  <span class="placeholder col-12"></span>
</p>
```

#### Popovers

![https://ibb.co/Dbjm2Rb](https://i.ibb.co/cvsRnrv/25.png)

```html
<button type="button" class="btn btn-lg btn-danger" data-bs-toggle="popover" data-bs-title="Popover title" data-bs-content="And here's some amazing content. It's very engaging. Right?">
    Click to toggle popover
</button>
```

![https://ibb.co/FJf18fq](https://i.ibb.co/hHnN2n1/26.png)

```html
<button type="button" class="btn btn-secondary" data-bs-container="body" data-bs-toggle="popover" data-bs-placement="top" data-bs-content="Top popover">
  Popover on top
</button>
<button type="button" class="btn btn-secondary" data-bs-container="body" data-bs-toggle="popover" data-bs-placement="right" data-bs-content="Right popover">
  Popover on right
</button>
<button type="button" class="btn btn-secondary" data-bs-container="body" data-bs-toggle="popover" data-bs-placement="bottom" data-bs-content="Bottom popover">
  Popover on bottom
</button>
<button type="button" class="btn btn-secondary" data-bs-container="body" data-bs-toggle="popover" data-bs-placement="left" data-bs-content="Left popover">
  Popover on left
</button>
```

#### Progress

![https://ibb.co/Mkr0QPN](https://i.ibb.co/7tPmLry/27.png)

```html
<div class="progress">
  <div class="progress-bar" role="progressbar" aria-label="Basic example" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress">
  <div class="progress-bar" role="progressbar" aria-label="Basic example" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress">
  <div class="progress-bar" role="progressbar" aria-label="Basic example" style="width: 50%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress">
  <div class="progress-bar" role="progressbar" aria-label="Basic example" style="width: 75%" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress">
  <div class="progress-bar" role="progressbar" aria-label="Basic example" style="width: 100%" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100"></div>
</div>
```

![https://ibb.co/DRHbHNN](https://i.ibb.co/LZXPXMM/28.png)

```html
<div class="progress">
  <div class="progress-bar" role="progressbar" aria-label="Example with label" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">25%</div>
</div>
```

![https://ibb.co/47Ff4QQ](https://i.ibb.co/HVK2GJJ/29.png)

```html
<div class="progress">
  <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-label="Animated striped example" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width: 75%"></div>
</div>
```

#### Scrollpy

##### Navbar

![https://ibb.co/wc3nYT6](https://i.ibb.co/qJXHxz1/30.png)

```html
<nav id="navbar-example2" class="navbar bg-light px-3 mb-3">
  <a class="navbar-brand" href="#">Navbar</a>
  <ul class="nav nav-pills">
    <li class="nav-item">
      <a class="nav-link" href="#scrollspyHeading1">First</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#scrollspyHeading2">Second</a>
    </li>
    <li class="nav-item dropdown">
      <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">Dropdown</a>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#scrollspyHeading3">Third</a></li>
        <li><a class="dropdown-item" href="#scrollspyHeading4">Fourth</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item" href="#scrollspyHeading5">Fifth</a></li>
      </ul>
    </li>
  </ul>
</nav>
<div data-bs-spy="scroll" data-bs-target="#navbar-example2" data-bs-root-margin="0px 0px -40%" data-bs-smooth-scroll="true" class="scrollspy-example bg-light p-3 rounded-2" tabindex="0">
  <h4 id="scrollspyHeading1">First heading</h4>
  <p>...</p>
  <h4 id="scrollspyHeading2">Second heading</h4>
  <p>...</p>
  <h4 id="scrollspyHeading3">Third heading</h4>
  <p>...</p>
  <h4 id="scrollspyHeading4">Fourth heading</h4>
  <p>...</p>
  <h4 id="scrollspyHeading5">Fifth heading</h4>
  <p>...</p>
</div>
```

##### Nested nav

![https://ibb.co/xDHNkq5](https://i.ibb.co/FKVFr47/31.png)

```html
<div class="row">
  <div class="col-4">
    <nav id="navbar-example3" class="h-100 flex-column align-items-stretch pe-4 border-end">
      <nav class="nav nav-pills flex-column">
        <a class="nav-link" href="#item-1">Item 1</a>
        <nav class="nav nav-pills flex-column">
          <a class="nav-link ms-3 my-1" href="#item-1-1">Item 1-1</a>
          <a class="nav-link ms-3 my-1" href="#item-1-2">Item 1-2</a>
        </nav>
        <a class="nav-link" href="#item-2">Item 2</a>
        <a class="nav-link" href="#item-3">Item 3</a>
        <nav class="nav nav-pills flex-column">
          <a class="nav-link ms-3 my-1" href="#item-3-1">Item 3-1</a>
          <a class="nav-link ms-3 my-1" href="#item-3-2">Item 3-2</a>
        </nav>
      </nav>
    </nav>
  </div>

  <div class="col-8">
    <div data-bs-spy="scroll" data-bs-target="#navbar-example3" data-bs-smooth-scroll="true" class="scrollspy-example-2" tabindex="0">
      <div id="item-1">
        <h4>Item 1</h4>
        <p>...</p>
      </div>
      <div id="item-1-1">
        <h5>Item 1-1</h5>
        <p>...</p>
      </div>
      <div id="item-1-2">
        <h5>Item 1-2</h5>
        <p>...</p>
      </div>
      <div id="item-2">
        <h4>Item 2</h4>
        <p>...</p>
      </div>
      <div id="item-3">
        <h4>Item 3</h4>
        <p>...</p>
      </div>
      <div id="item-3-1">
        <h5>Item 3-1</h5>
        <p>...</p>
      </div>
      <div id="item-3-2">
        <h5>Item 3-2</h5>
        <p>...</p>
      </div>
    </div>
  </div>
</div>
```

##### List group

![https://ibb.co/VSByRyk](https://i.ibb.co/k8cnjnP/32.png)

```html
<div class="row">
  <div class="col-4">
    <div id="list-example" class="list-group">
      <a class="list-group-item list-group-item-action" href="#list-item-1">Item 1</a>
      <a class="list-group-item list-group-item-action" href="#list-item-2">Item 2</a>
      <a class="list-group-item list-group-item-action" href="#list-item-3">Item 3</a>
      <a class="list-group-item list-group-item-action" href="#list-item-4">Item 4</a>
    </div>
  </div>
  <div class="col-8">
    <div data-bs-spy="scroll" data-bs-target="#list-example" data-bs-smooth-scroll="true" class="scrollspy-example" tabindex="0">
      <h4 id="list-item-1">Item 1</h4>
      <p>...</p>
      <h4 id="list-item-2">Item 2</h4>
      <p>...</p>
      <h4 id="list-item-3">Item 3</h4>
      <p>...</p>
      <h4 id="list-item-4">Item 4</h4>
      <p>...</p>
    </div>
  </div>
</div>
```

##### Simple anchors

![https://ibb.co/n3kwrC9](https://i.ibb.co/3fhT1z2/33.png)

```html
<div class="row">
  <div class="col-4">
    <div id="simple-list-example" class="d-flex flex-column gap-2 simple-list-example-scrollspy text-center">
      <a class="p-1 rounded" href="#simple-list-item-1">Item 1</a>
      <a class="p-1 rounded" href="#simple-list-item-2">Item 2</a>
      <a class="p-1 rounded" href="#simple-list-item-3">Item 3</a>
      <a class="p-1 rounded" href="#simple-list-item-4">Item 4</a>
      <a class="p-1 rounded" href="#simple-list-item-5">Item 5</a>
    </div>
  </div>
  <div class="col-8">
    <div data-bs-spy="scroll" data-bs-target="#simple-list-example" data-bs-offset="0" data-bs-smooth-scroll="true" class="scrollspy-example" tabindex="0">
      <h4 id="simple-list-item-1">Item 1</h4>
      <p>...</p>
      <h4 id="simple-list-item-2">Item 2</h4>
      <p>...</p>
      <h4 id="simple-list-item-3">Item 3</h4>
      <p>...</p>
      <h4 id="simple-list-item-4">Item 4</h4>
      <p>...</p>
      <h4 id="simple-list-item-5">Item 5</h4>
      <p>...</p>
    </div>
  </div>
</div>
```

#### Spinners

##### Border

```html
<div class="spinner-border" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
<div class="spinner-border text-primary" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
<div class="spinner-border text-secondary" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
<div class="spinner-border text-success" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
<div class="spinner-border text-danger" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
<div class="spinner-border text-warning" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
<div class="spinner-border text-info" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
<div class="spinner-border text-light" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
<div class="spinner-border text-dark" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
```

##### Growing

```html
<div class="spinner-grow" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
<div class="spinner-grow text-primary" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
<div class="spinner-grow text-secondary" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
<div class="spinner-grow text-success" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
<div class="spinner-grow text-danger" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
<div class="spinner-grow text-warning" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
<div class="spinner-grow text-info" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
<div class="spinner-grow text-light" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
<div class="spinner-grow text-dark" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
```

##### Placement

```html
<div class="d-flex justify-content-center">
  <div class="spinner-border" role="status">
    <span class="visually-hidden">Loading...</span>
  </div>
</div>
```

```html
<div class="d-flex align-items-center">
  <strong>Loading...</strong>
  <div class="spinner-border ms-auto" role="status" aria-hidden="true"></div>
</div>
```

```html
<div class="clearfix">
  <div class="spinner-border float-end" role="status">
    <span class="visually-hidden">Loading...</span>
  </div>
</div>
```

```html
<div class="text-center">
  <div class="spinner-border" role="status">
    <span class="visually-hidden">Loading...</span>
  </div>
</div>
```

#### Toast

![https://ibb.co/YjB0XsL](https://i.ibb.co/dK4mtY5/34.png)

```html
<button type="button" class="btn btn-primary" id="liveToastBtn">Show live toast</button>

<div class="toast-container position-fixed bottom-0 end-0 p-3">
  <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
    <div class="toast-header">
      <img src="..." class="rounded me-2" alt="...">
      <strong class="me-auto">Bootstrap</strong>
      <small>11 mins ago</small>
      <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
    </div>
    <div class="toast-body">
      Hello, world! This is a toast message.
    </div>
  </div>
</div>
```

#### Tooltip

![https://ibb.co/DL3vnzV](https://i.ibb.co/wYDP1B0/35.png)

```html
<button type="button" class="btn btn-secondary"
        data-bs-toggle="tooltip" data-bs-placement="top"
        data-bs-custom-class="custom-tooltip"
        data-bs-title="This top tooltip is themed via CSS variables.">
  Custom tooltip
</button>
```

![https://ibb.co/pQtmHPJ](https://i.ibb.co/ypw3zRW/36.png)

```html
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="top" data-bs-title="Tooltip on top">
  Tooltip on top
</button>
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="right" data-bs-title="Tooltip on right">
  Tooltip on right
</button>
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="Tooltip on bottom">
  Tooltip on bottom
</button>
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip" data-bs-placement="left" data-bs-title="Tooltip on left">
  Tooltip on left
</button>
```

### Forms

#### Overview

![https://ibb.co/jMqmpTV](https://i.ibb.co/swcnB25/37.png)

```html
<form>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1">
  </div>
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

![https://ibb.co/jDTh5yc](https://i.ibb.co/x6Dhs1p/38.png)

```html
<form>
  <fieldset disabled>
    <legend>Disabled fieldset example</legend>
    <div class="mb-3">
      <label for="disabledTextInput" class="form-label">Disabled input</label>
      <input type="text" id="disabledTextInput" class="form-control" placeholder="Disabled input">
    </div>
    <div class="mb-3">
      <label for="disabledSelect" class="form-label">Disabled select menu</label>
      <select id="disabledSelect" class="form-select">
        <option>Disabled select</option>
      </select>
    </div>
    <div class="mb-3">
      <div class="form-check">
        <input class="form-check-input" type="checkbox" id="disabledFieldsetCheck" disabled>
        <label class="form-check-label" for="disabledFieldsetCheck">
          Can't check this
        </label>
      </div>
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </fieldset>
</form>
```

#### Form control

##### Read-Only

![https://ibb.co/9pgZkMt](https://i.ibb.co/XWLYrw8/39.png)

```html
<input class="form-control" type="text" value="Readonly input here..." aria-label="readonly input example" readonly>
```

##### Read-Only plain text

![https://ibb.co/XZt4KDD](https://i.ibb.co/GvRJ899/40.png)

```html
  <div class="mb-3 row">
    <label for="staticEmail" class="col-sm-2 col-form-label">Email</label>
    <div class="col-sm-10">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="email@example.com">
    </div>
  </div>
  <div class="mb-3 row">
    <label for="inputPassword" class="col-sm-2 col-form-label">Password</label>
    <div class="col-sm-10">
      <input type="password" class="form-control" id="inputPassword">
    </div>
  </div>
```

##### File Input

![https://ibb.co/chjkyZ4](https://i.ibb.co/4RHKFXh/41.png)

```html
<div class="mb-3">
  <label for="formFile" class="form-label">Default file input example</label>
  <input class="form-control" type="file" id="formFile">
</div>
<div class="mb-3">
  <label for="formFileMultiple" class="form-label">Multiple files input example</label>
  <input class="form-control" type="file" id="formFileMultiple" multiple>
</div>
<div class="mb-3">
  <label for="formFileDisabled" class="form-label">Disabled file input example</label>
  <input class="form-control" type="file" id="formFileDisabled" disabled>
</div>
<div class="mb-3">
  <label for="formFileSm" class="form-label">Small file input example</label>
  <input class="form-control form-control-sm" id="formFileSm" type="file">
</div>
<div>
  <label for="formFileLg" class="form-label">Large file input example</label>
  <input class="form-control form-control-lg" id="formFileLg" type="file">
</div>
```

##### Color

```html
<label for="exampleColorInput" class="form-label">Color picker</label>
<input type="color" class="form-control form-control-color" id="exampleColorInput" value="#563d7c" title="Choose your color">
```

##### Datalists

```html
<label for="exampleDataList" class="form-label">Datalist example</label>
<input class="form-control" list="datalistOptions" id="exampleDataList" placeholder="Type to search...">
<datalist id="datalistOptions">
  <option value="San Francisco">
  <option value="New York">
  <option value="Seattle">
  <option value="Los Angeles">
  <option value="Chicago">
</datalist>
```

#### Select

![https://ibb.co/YPMjGCs](https://i.ibb.co/vVGz8Fn/42.png)

```html
<select class="form-select" aria-label="Default select example">
  <option selected>Open this select menu</option>
  <option value="1">One</option>
  <option value="2">Two</option>
  <option value="3">Three</option>
</select>
```

![https://ibb.co/dPpC4WC](https://i.ibb.co/ZBg4zL4/43.png)

```html
<select class="form-select" aria-label="Disabled select example" disabled>
  <option selected>Open this select menu</option>
  <option value="1">One</option>
  <option value="2">Two</option>
  <option value="3">Three</option>
</select>
```

#### Check

![https://ibb.co/mqw57L8](https://i.ibb.co/Wywv1bt/44.png)

```html
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
  <label class="form-check-label" for="flexCheckDefault">
    Default checkbox
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked" checked>
  <label class="form-check-label" for="flexCheckChecked">
    Checked checkbox
  </label>
</div>
```

![https://ibb.co/JmzyKkF](https://i.ibb.co/ckNC1TX/45.png)

```html
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="flexCheckIndeterminateDisabled" disabled>
  <label class="form-check-label" for="flexCheckIndeterminateDisabled">
    Disabled indeterminate checkbox
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="flexCheckDisabled" disabled>
  <label class="form-check-label" for="flexCheckDisabled">
    Disabled checkbox
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="flexCheckCheckedDisabled" checked disabled>
  <label class="form-check-label" for="flexCheckCheckedDisabled">
    Disabled checked checkbox
  </label>
</div>
```

![https://ibb.co/rmm15JZ](https://i.ibb.co/377LSH0/48.png)

```html
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDefault">
  <label class="form-check-label" for="flexSwitchCheckDefault">Default switch checkbox input</label>
</div>
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckChecked" checked>
  <label class="form-check-label" for="flexSwitchCheckChecked">Checked switch checkbox input</label>
</div>
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckDisabled" disabled>
  <label class="form-check-label" for="flexSwitchCheckDisabled">Disabled switch checkbox input</label>
</div>
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckCheckedDisabled" checked disabled>
  <label class="form-check-label" for="flexSwitchCheckCheckedDisabled">Disabled checked switch checkbox input</label>
</div>
```

#### Radio

![https://ibb.co/3yHXBN3](https://i.ibb.co/0j3NhM7/46.png)

```html
<div class="form-check">
  <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
  <label class="form-check-label" for="flexRadioDefault1">
    Default radio
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked>
  <label class="form-check-label" for="flexRadioDefault2">
    Default checked radio
  </label>
</div>
```

![https://ibb.co/H2xNrZs](https://i.ibb.co/GJtsVmL/47.png)

```html
<div class="form-check">
  <input class="form-check-input" type="radio" name="flexRadioDisabled" id="flexRadioDisabled" disabled>
  <label class="form-check-label" for="flexRadioDisabled">
    Disabled radio
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="radio" name="flexRadioDisabled" id="flexRadioCheckedDisabled" checked disabled>
  <label class="form-check-label" for="flexRadioCheckedDisabled">
    Disabled checked radio
  </label>
</div>
```

#### Range

![https://ibb.co/f4H4yLG](https://i.ibb.co/yWqWZ7B/49.png)

```html
<label for="customRange1" class="form-label">Example range</label>
<input type="range" class="form-range" id="customRange1">
```

![https://ibb.co/y4PwSH5](https://i.ibb.co/NTC8Scp/50.png)

```html
<label for="disabledRange" class="form-label">Disabled range</label>
<input type="range" class="form-range" id="disabledRange" disabled>
```

##### Min and Max

```html
<label for="customRange2" class="form-label">Example range</label>
<input type="range" class="form-range" min="0" max="5" id="customRange2">
```

##### Steps

```html
<label for="customRange3" class="form-label">Example range</label>
<input type="range" class="form-range" min="0" max="5" step="0.5" id="customRange3">
```

#### Input Group

![https://ibb.co/TwQrth7](https://i.ibb.co/zm3NZfB/51.png)

```html
<div class="input-group mb-3">
  <span class="input-group-text" id="basic-addon1">@</span>
  <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1">
</div>

<div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Recipient's username" aria-label="Recipient's username" aria-describedby="basic-addon2">
  <span class="input-group-text" id="basic-addon2">@example.com</span>
</div>

<label for="basic-url" class="form-label">Your vanity URL</label>
<div class="input-group mb-3">
  <span class="input-group-text" id="basic-addon3">https://example.com/users/</span>
  <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3">
</div>

<div class="input-group mb-3">
  <span class="input-group-text">$</span>
  <input type="text" class="form-control" aria-label="Amount (to the nearest dollar)">
  <span class="input-group-text">.00</span>
</div>

<div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Username" aria-label="Username">
  <span class="input-group-text">@</span>
  <input type="text" class="form-control" placeholder="Server" aria-label="Server">
</div>

<div class="input-group">
  <span class="input-group-text">With textarea</span>
  <textarea class="form-control" aria-label="With textarea"></textarea>
</div>
```

#### Floating labels

![https://ibb.co/9HsRTKn](https://i.ibb.co/yFWLyv0/52.png)

```html
<div class="form-floating mb-3">
  <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
  <label for="floatingInput">Email address</label>
</div>
<div class="form-floating">
  <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
  <label for="floatingPassword">Password</label>
</div>
```

### Extends

#### icons

- [Icons · Bootstrap v5.2 (getbootstrap.com)](https://getbootstrap.com/docs/5.2/extend/icons/)

## Animation

- [Animate.css | A cross-browser library of CSS animations.](https://animate.style/)

```css
<head>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
</head>
```

```css
<h1 class="animate__animated animate__bounce">An animated element</h1>
<div class="animate__animated animate__bounce animate__delay-2s">Example</div>
<div class="animate__animated animate__bounce animate__faster">Example</div>
<div class="animate__animated animate__bounce animate__repeat-2">Example</div>
```

## Other

- [토픽 | 디자이너스 (designus.io)](https://designus.io/topic)

- [Swiper - The Most Modern Mobile Touch Slider (swiperjs.com)](https://swiperjs.com/)


# JavaScript

## ECMA Script (JavaScript Core)

### 변수와 식별자

- 식별자(identifier)는 변수를 구분할 수 있는 변수명을 말함
- 식별자는 반드시 문자, 달러($) 또는 밑줄(_)로 시작
- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작
- 예약어 사용 불가능
  - 예약어 예시: for, if, function 등

```javascript
// 선언 (Declaration) : 변수를 생성하는 행위 또는 시점
// 할당 (Assignment) : 선언된 변수에 값을 저장하는 행위 또는 시점
// 초기화 (Initialization) : 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

let foo          // 선언
console.log(foo) // undefined

foo = 11         // 할당
console.log(foo) // 11

let bar = 0      // 선언 + 할당
console.log(bar) // 0
```

#### let, const

| ![https://ibb.co/KDW26Vk](https://i.ibb.co/FXz568M/1.png) | ![https://ibb.co/mhPZg3F](https://i.ibb.co/SVZYGz7/2.png) |
| :-------------------------------------------------------: | :-------------------------------------------------------: |
|                     let (재할당 가능)                     |                   const (재할당 불가능)                   |

| ![https://ibb.co/89N1VXw](https://i.ibb.co/HqB5QXy/3.png) | ![https://ibb.co/3pRMDNC](https://i.ibb.co/8rYdW57/4.png) |
| :-------------------------------------------------------: | :-------------------------------------------------------: |
|                    let (재선언 불가능)                    |                   const (재선언 불가능)                   |

```javascript
// 블록 스코프 (block scope)
// if, for, 함수 등의 중괄호 내부를 가리킴
// 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

let x = 1

if (x === 1) {
  let x = 2
  console.log(x)  // 2
}

console.log(x)    // 1
```

#### var

- ES6 이전에 변수를 선언할 때 사용되던 키워드
- 호이스팅되는 특성으로 인해 예기치 못한 문제 발생 가능
  - 따라서 ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장

```javascript
var n = 10 // 선언 및 초기값 할당
var n = 50 // 재할당

console.log(n) // 50

// var로 선언한 변수는 재선언 및 재할당 모두 가능
```

```javascript
// 함수 스코프 (function scope)
// 함수의 중괄호 내부를 가리킴
// 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

function foo() {
  var x = 5
  console.log(x)  // 5
}

// ReferenceError: x is not defined
console.log(x)
```

#### hoisting (호이스팅)

```javascript
console.log(username) // undefined
var username = '홍길동'

console.log(email) // Uncaught ReferenceError
let email = 'gildong@gmail.com'

console.log(age)   // Uncaught ReferenceError
const age = 50
```

- 변수를 선언 이전에 참조할 수 있는 현상
- 변수 선언 이전의 위치에서 접근 시 undefined를 반환
- 자바스크립트는 모든 선언을 호이스팅함
  - 즉, var, let, const 모두 호이스팅이 발생
  -  var는 선언과 초기화가 동시에 발생 하여 일시적 사각지대가 존재하지 않음

#### let, const, var 비교

| 키워드 | 재선언 | 재할당 |   스코프    |     비고      |
| :----: | :----: | :----: | :---------: | :-----------: |
|  let   |   X    |   O    | 블록 스코프 | ES6부터 도입  |
| const  |   X    |   X    | 블록 스코프 | ES6부터 도입  |
|  var   |   O    |   O    | 함수 스코프 | 사용하지 않음 |

### 데이터 타입

![https://ibb.co/XFcJhVJ](https://i.ibb.co/9yQYFGY/5.png)

- 자바스크립트의 모든 값은 특정한 데이터 타입을 가짐
- 크게 원시 타입 (Primitive type)과 참조 타입 (Reference type)으로 분류됨

#### 원시 타입 (Primitive type)

```javascript
let message = '안녕하세요!' // 1. message 선언 및 할당

let greeting = message    // 2. greeting에 message 복사
console.log(greeting)     // 3. '안녕하세요!' 출력

message = 'Hello, world!' // 4. message 재할당
console.log(greeting)     // 5. '안녕하세요!' 출력

// 즉, 원시 타입은 실제 해당 타입의 값을 변수에 저장한다.
```

- 객체 (object)가 아닌 기본 타입
- 변수에 해당 타입의 값이 담김
- 다른 변수에 복사할 때 실제 값이 복사됨

##### 숫자 (Number) 타입

```javascript
const a = 13        // 양의 정수
const b = -5        // 음의 정수
const c = 3.14      // 실수
const d = 2.998e8   // 거듭제곱
const e = Infinity  // 양의 무한대
const f = -Infinity // 음의 무한대
const g = NaN       // 산술 연산 불가
```

- 정수, 실수 구분 없는 하나의 숫자 타입
- 부동소수점 형식을 따름
- NaN (Not-A-Number) : 계산 불가능한 경우 반환되는 값
  - ex) 'Angel' / 1004 => NaN

##### 문자열 (String) 타입

```javascript
const firstName = 'Brandan'
const lastName = 'Eich'
const fullName = `${firstName} ${lastName}`

console.log(fullName) // Brandan Eich
```

- 텍스트 데이터를 나타내는 타입
- 16비트 유니코드 문자의 집합
- 작은따옴표 또는 큰따옴표 모두 가능
- 템플릿 리터럴 (Template Literal)
  - ES6부터 지원
  - 따옴표 대신 backtick(\`\`)으로 표현
  - ${ expression } 형태로 표현식 삽입 가능

##### undefined

```javascript
let firstName
console.log(firstName) // undefined
```

- 변수의 값이 없음을 나타내는 데이터 타입
- 변수 선언 이후 직접 값을 할당하지 않으면, 자동으로 undefined가 할당됨

##### null

```javascript
let firstName = null
console.log(firstName) // null

typeof null // object
```

- 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입
- (참고) null 타입과 typeof 연산자
  - typeof 연산자 : 자료형 평가를 위한 연산자
  - null 타입은 [ECMA 명세의 원시 타입](https://tc39.es/ecma262/#sec-primitive-value)의 정의에 따라 원시 타입에 속함
  - typeof 연산자의 결과는 객체(object)로 표현됨 ([참고 자료](https://2ality.com/2013/10/typeof-null.html))

##### Boolean 타입

```javascript
let isAdmin = true
console.log(isAdmin) // true

isAdmin = false
console.log(isAdmin) // false
```

- 논리적 참 또는 거짓을 나타내는 타입

- true 또는 false로 표현

- 조건문 또는 반복문에서 유용하게 사용

  - (참고) 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 [자동 형변환 규칙](https://tc39.es/ecma262/#sec-type-conversion)에 따라 true 또는 false로 변환됨

  - (참고) [ToBoolean Conversions (자동 형변환)](https://tc39.es/ecma262/#sec-toboolean) 정리

    | 데이터 타입 |    거짓    |        참        |
    | :---------: | :--------: | :--------------: |
    |  undefined  | 항상 거짓  |        X         |
    |    null     | 항상 거짓  |        X         |
    |   Number    | 0, -0, NaN | 나머지 모든 경우 |
    |   String    | 빈 문자열  | 나머지 모든 경우 |
    |   Object    |     X      |     항상 참      |

#### 참조 타입 (Reference type)

```javascript
const message = ['안녕하세요!'] // 1. message 선언 및 할당

const greeting = message    // 2. greeting에 message 복사
console.log(greeting)     // 3. ['안녕하세요!'] 출력

message[0] = 'Hello, world!' // 4. message 재할당
console.log(greeting)     // 5. ['Hello, world!'] 출력

// 즉, 참조 타입은 해당 객체를 참조할 수 있는 참조 값을 저장한다.
```

- 객체 (object) 타입의 자료형
- 변수에 해당 객체의 참조 값이 담김
- 다른 변수에 복사할 때 참조 값이 복사됨

### 연산자

#### 할당 연산자

```javascript
let x = 0;

x += 10
console.log(x) // 10

x -= 3
console.log(x) // 7

x *= 10
console.log(x) // 70

x /= 10
console.log(x) // 7

x++            // += 연산자와 동일
console.log(x) // 8

x--            // -= 연산자와 동일
console.log(x) // 7
```

- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
- 다양한 연산에 대한 단축 연산자 지원
- (참고) Increment 및 Decrement 연산자
  - Increment(++): 피연산자의 값을 1 증가시키는 연산자
  - Decrement(--): 피연산자의 값을 1 감소시키는 연산자
  - [Airbnb Style Guide](https://github.com/airbnb/javascript#variables--unary-increment-decrement)에서는 ‘+=’ 또는 ‘-=’와 같이 더 분명한 표현으로 적을 것을 권장

#### 비교 연산자

```javascript
const numOne = 1
const numTwo = 100
console.log(numOne < numTwo) // true

const charOne = 'a'
const charTwo = 'z'
console.log(charOne > charTwo) // false
```

- 피연산자를 비교하고 결과값을 boolean으로 반환하는 연산자
- 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교
  - ex) 알파벳끼리 비교할 경우
    - 알파벳 순서상 후순위가 더 큼
    - 소문자가 대문자보다 더 큼

#### 동등 비교 연산자 (==)

```javascript
const a = 1004
const b = '1004'
console.log(a == b) // true

const c = 1
const d = true
console.log(c == d) // true

// 자동 타입 변환 예시
console.log(a + b) // 10041004
console.log(c + d) // 2
```

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 비교할 때 [암묵적 타입 변환](https://262.ecma-international.org/5.1/#sec-11.9.3)을 통해 타입을 일치시킨 후 같은 값인지 비교

- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
- 예상치 못한 결과가 발생할 수 있으므로 [특별한 경우](https://google.github.io/styleguide/jsguide.html#features-equality-checks-exceptions)를 제외하고 사용하지 않음

#### 일치 비교 연산자 (===)

```javascript
const a = 1004
const b = '1004'
console.log(a === b) // false

const c = 1
const d = true
console.log(c === d) // false
```

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- [엄격한 비교](https://262.ecma-international.org/5.1/#sec-11.9.6)가 이뤄지며 암묵적 타입 변환이 발생하지 않음
  - 엄격한 비교 : 두 비교 대상의 타입과 값 모두 같은지 비교

#### 논리 연산자

```javascript
// and 연산
console.log(true && false) // false
console.log(true && true)  // true
console.log(1 && 0)        // 0
console.log(4 && 7)        // 7
console.log('' && 5)       // ''

// or 연산
console.log(true || false)   // true
console.log(false || false)  // false
console.log(1 || 0)          // 1
console.log(4 || 7)          // 4
console.log('' || 5)         // 5

// not 연산
console.log(!true)       // false
console.log(!'Bonjour!') // false
```

- 세 가지 논리 연산자로 구성
  - and 연산은 '&&' 연산자를 이용
  - or 연산은 '||' 연산자를 이용
  - not 연산은 '!' 연산자를 이용
- 단축 평가 지원
  - ex) false && true => false
  - ex) true || false => true

#### 삼항 연산자 (Ternary Operator)

```javascript
console.log(true ? 1 : 2) // 1
console.log(false ? 1 : 2) // 2

const result = Math.PI > 4 ? 'Yes' : 'No'
console.log(result) // No
```

- 세 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
- 가장 왼쪽의 조건식이 참이면 콜론(:) 앞의 값을 사용하고 그렇지 않으면 콜론(:) 뒤의 값을 사용
- 삼항 연산자의 결과 값이기 때문에 변수에 할당 가능
- (참고) [한 줄에 표기하는 것을 권장](https://github.com/airbnb/javascript#comparison--nested-ternaries)

### 조건문

#### if statement

```javascript
if (condition) {
  // do something
} else if (condition) {
  // do something
} else {
  // do something
}
```

```javascript
const nation = 'Korea'

if (nation === 'Korea') {
    console.log('안녕하세요!')
} else if (nation === 'France') {
    console.log('Bonjour!')
} else {
    console.log('Hello!')
}
```

- 조건 표현식의 결과값을 Boolean 타입으로 변환 후 참/거짓을 판단
- if, else if, else
  - 조건은 소괄호(condition) 안에 작성
  - 실행할 코드는 중괄호{} 안에 작성
  - 블록 스코프 생성

#### switch statement

```javascript
switch(expression) {
  case 'first value': {
    // do something
    [break]
  }
  case 'second value': {
  	// do something
    [break]
  }
  [default: {
    // do something
  }]
}
```

```javascript
const nation = 'Korea'

switch(nation) {
    case 'Korea': {
        console.log('안녕하세요!')
        break
    }
    case 'France': {
        console.log('Bonjour!')
        break
    }
    default: {
        console.log('Hello!')
    }
}
// break 문이 없으면 모든 log를 출력하게 됨(Fall-through)
```

- 조건 표현식의 결과값이 어느 값(case)에 해당하는지 판별
- 주로 특정 변수의 값에 따라 조건을 분기할 때 활용
  - 조건이 많아질 경우 if문보다 가독성이 나을 수 있음
- 표현식 (expression)의 결과값을 이용한 조건문
- 표현식의 결과값과 case 문의 오른쪽 값을 비교
- break 및 default 문은 [선택적]으로 사용 가능
- break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행

### 반복문

- while
- for
- for...in
  - 주로 객체(object)의 속성들을 순회할 때 사용
  - 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음
- for...of
  - 반복 가능한(iterable) 객체를 순회하며 값을 꺼낼 때 사용
  - 반복 가능한(iterable) 객체의 종류: Array, Map, Set, String 등

#### while

```javascript
while (condition) {
    // do something
}
```

```javascript
let i = 0

while (i < 6) {
    console.log(i) // 0 1 2 3 4 5
}
```

- 조건문이 참(true)인 동안 반복 시행
- 조건은 소괄호 안에 작성
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성

#### for

```javascript
for (initialization; condition; expression) {
    // do something
}
```

```javascript
for (let i = 0; i < 6; i++) {
    console.log(i) // 0 1 2 3 4 5
}
```

- 세미콜론(;)으로 구분되는 세 부분 으로 구성
- initialization
  - 최초 반복문 진입 시 1회만 실행되는 부분
- condition
  - 매 반복 시행 전 평가되는 부분
- expression
  - 매 반복 시행 이후 평가되는 부분
- 블록 스코프 생성

#### for...in

```javascript
for (variable in object) {
  // do something
}
```

```javascript
// object(객체) => key-value로 이루어진 자료구조
const capitals = {
  korea: 'seoul',
  france: 'paris',
  USA: 'washington D.C.'
}

for (let capital in capitals) {
  console.log(capital) // korea, france, USA
}
```

- 객체(object)의 속성(key)들을 순회할 때 사용
- 배열도 순회 가능하지만 권장하지 않음
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성

#### for...of

```javascript
for (variable of iterables) {
  // do something
}
```

```javascript
const fruits = ['딸기', '바나나', '메론']

for (let fruit of fruits) {
  fruit = fruit + '!'
  console.log(fruit)
}
```

- 반복 가능한(iterable) 객체를 순회하며 값을 꺼낼 때 사용 
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성

### 함수 (Function)

- 참조 타입 중 하나로서 function 타입에 속함
- JavaScript에서 함수를 정의하는 방법은 주로 2가지로 구분
  - 함수 선언식 (function declaration)
  - 함수 표현식 (function expression)
- JavaScript의 함수는 [일급 객체(First-class citizen)](https://developer.mozilla.org/ko/docs/Glossary/First-class_Function)에 해당
  - 일급 객체 : 다음의 조건들을 만족하는 객체를 의미함
    - 변수에 할당 가능
    - 함수의 매개변수로 전달 가능
    - 함수의 반환 값으로 사용 가능

#### 함수 선언식

```javascript
function name(args) {
  // do something
}
```

```javascript
function add(num1, num2) {
  return num1 + num2
}

add(1, 2)
```

- 함수의 이름과 함께 정의하는 방식
- 3가지 부분으로 구성
  - 함수의 이름 (name)
  - 매개변수 (args)
  - 함수 body (중괄호 내부)

#### 함수 표현식

```javascript
const name = function (args) {
  // do something
}
```

```javascript
const add = function (num1, num2) {
  return num1 + num2
}
add(1, 2)
```

- 함수를 표현식 내에서 정의하는 방식
  - 표현식 : 어떤 하나의 값으로 결정되는 코드의 단위
- 함수의 이름을 생략하고 익명 함수로 정의 가능
  - 익명 함수 (anonymous function): 이름이 없는 함수
  - 익명 함수는 함수 표현식에서만 가능
- 3가지 부분으로 구성
  - 함수의 이름 (생략 가능) 
  - 매개변수 (args)
  - 몸통 (중괄호 내부)

#### 기본 인자

```javascript
const greeting = function (name = 'Anonymous') {
  return `Hi ${name}`
}

greeting() // Hi Anonymous
```

- 인자 작성 시 ‘=’ 문자 뒤 기본 인자 선언 가능

#### 매개변수와 인자의 개수 불일치 허용

```javascript
// 매개변수보다 인자의 개수가 많을 경우
const noArgs = function () {
  return 0
}

noArgs(1, 2, 3) // 0

const twoArgs = function (arg1, arg2) {
  return [arg1, arg2]
}

twoArgs(1, 2, 3) // [1, 2]
```

```javascript
// 매개변수보다 인자의 개수가 적을 경우
const threeArgs = function (arg1, arg2, arg3) {
  return [arg1, arg2, arg3]
}

threeArgs()     // [undefined, undefined, undefined]
threeArgs(1)    // [1, undefined, undefined]
threeArgs(1, 2) // [1, 2, undefined]
```

#### Rest Parameter

```javascript
const restOpr = function (arg1, arg2, ...restArgs) {
  return [arg1, arg2, restArgs]
}

restArgs(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
restArgs(1, 2) // [1, 2, []]
// 만약 rest parameter로 처리한 매개변수에 인자가 넘어오지 않을 경우에는, 빈 배열로 처리
```

- rest parameter(…)를 사용하면 함수가 정해지지 않은 수의 매개변수를 배열로 받음 
  - (python 의 *args 와 유사)

#### Spread operator

```javascript
const spreadOpr = function (arg1, arg2, arg3) {
  return arg1 + arg2 + arg3
}

const numbers = [1, 2, 3]
spreadOpr(...numbers) // 6
```

- spread operator(…)를 사용하면 배열 인자를 전개하여 전달 가능

#### 선언식 vs 표현식

- 공통점 : 데이터 타입, 함수 구성 요소 (이름, 매개변수, 몸통)
- 차이점
  - 함수 선언식 : 익명 함수 불가능, 호이스팅 O
  - 함수 표현식 : 익명 함수 가능, 호이스팅 X

##### 함수의 타입

```javascript
// 함수 표현식
const add = function (args) { }

// 함수 선언식
function sub(args) { }

console.log(typeof add) // function
console.log(typeof sub) // function
```

- 선언식 함수와 표현식 함수 모두 타입은 function으로 동일

##### 호이스팅(hoisting) – 함수 선언식

```javascript
add(2, 7) // 9

function add (num1, num2) {
    return num1 + num2
}
```

- 함수 선언식으로 선언한 함수는 var로 정의한 변수처럼 hoisting 발생
- 함수 호출 이후에 선언 해도 동작

##### 호이스팅(hoisting) – 함수 표현식

```javascript
sub(7, 2) // Uncaught ReferenceError : Cannot access 'sub' before initialization

const sub = function (num1, num2) {
    return num1 - num2
}
```

- 함수 표현식으로 선언한 함수는 함수 정의 전에 호출 시 에러 발생
- 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름

```javascript
console.log(sub) // undefined
sub(7, 2) // Uncaught TypeError : sub is not a function

var sub = function (num1, num2) {
    return num1 - num2
}
```

- 함수 표현식을 var 키워드로 작성한 경우,  변수가 선언 전 undefined로 초기화 되어 다른 에러가 발생

### 화살표 함수 (Arror Function)

```javascript
const arrow1 = function (name) { 
  return `hello, ${name}`
}

// 1. function 키워드 삭제
const arrow2 = (name) => { return `hello, ${name}` }

// 2. 매개변수가 1개일 경우에만 ( ) 생략 가능
const arrow3 = name => { return `hello, ${name}` }

// 3. 함수 몸통이 return을 포함한 표현식 1개일 경우에 { } & return 삭제 가능
const arrow4 = name => `hello, ${name}`
```

- 함수를 비교적 간결하게 정의할 수 있는 문법
- function 키워드 생략 가능
- 함수의 매개변수가 단 하나 뿐이라면, '( )'도 생략 가능
- 함수 몸통이 표현식 하나라면 '{ }'와 return도 생략 가능

### 문자열 (String)

- 주요 메소드 목록 (참고 : [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#instance_methods), [ECMA262](https://tc39.es/ecma262/#sec-string-objects))

  | 메소드   | 설명                                       | 비고                                         |
  | :------- | :----------------------------------------- | :------------------------------------------- |
  | includes | 특정 문자열의 존재 여부를 참/거짓으로 반환 |                                              |
  | split    | 문자열을 토큰 기준으로 나눈 배열 반환      | 인자가 없으면 기존 문자열을 배열에 담아 반환 |
  | replace  | 해당 문자열을 대상 문자열로 교체하여 반환  | replaceAll                                   |
  | trim     | 문자열의 좌우 공백을 제거하여 반환         | trimStart, trimEnd                           |

#### includes

```javascript
const str = 'a santa at nasa’

str.includes('santa') // true
str.includes('asan') // false
```

- string.includes(value)
  - 문자열에 value가 존재하는지 판별 후 참 또는 거짓 반환

#### split

```javascript
const str = 'a cup’

str.split() // ['a cup’]
str.split('') // ['a', ' ', 'c', 'u', 'p']
str.split(' ') // ['a', 'cup']
```

- string.split(value)
  - value가 없을 경우, 기존 문자열을 배열에 담아 반환
  - value가 빈 문자열일 경우 각 문자로 나눈 배열을 반환
  - value가 기타 문자열일 경우, 해당 문자열로 나눈 배열을 반환

#### replace

```javascript
const str = 'a b c d'

str.replace(' ', '-') // 'a-b c d'
str.replaceAll(' ', '-') // 'a-b-c-d'
```

- string.replace(from, to)
  - 문자열에 from 값이 존재할 경우, 하나만 to 값으로 교체하여 반환
- string.replaceAll(from, to)
  - 문자열에 from 값이 존재할 경우, 모두 to 값으로 교체하여 반환

#### trim

```javascript
const str = '    hello    '

str.trim()      // 'hello'
str.trimStart() // 'hello    '
str.trimEnd()   // '    hello'
```

- string.trim()
  - 문자열 시작과 끝의 모든 공백 문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환
- string.trimStart()
  - 문자열 시작의 공백 문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환
- string.trimEnd()
  - 문자열 끝의 공백 문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환

### 배열 (Arrays)

```javascript
const numbers = [1, 2, 3, 4, 5]

console.log(numbers[0])     // 1
console.log(numbers[-1])    // undefined
console.log(numbers.length) // 5

console.log(numbers[numbers.length - 1]) // 5
console.log(numbers[numbers.length - 2]) // 4
console.log(numbers[numbers.length - 3]) // 3
console.log(numbers[numbers.length - 4]) // 2
console.log(numbers[numbers.length - 5]) // 1
```

- 키와 속성들을 담고 있는 참조 타입의 객체(object)

- 순서를 보장하는 특징이 있음

- 주로 대괄호를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능

- 배열의 길이는 array.length 형태로 접근 가능

  - 배열의 마지막 원소는 array.length – 1로 접근

- 주요 메소드 - 기본 (참고 : [MDN](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array#%EC%9D%B8%EC%8A%A4%ED%84%B4%EC%8A%A4_%EB%A9%94%EC%84%9C%EB%93%9C), [ECMA262](https://tc39.es/ecma262/#sec-properties-of-the-array-constructor))

  | 메소드          | 설명                                             | 비고                     |
  | --------------- | ------------------------------------------------ | ------------------------ |
  | reverse         | 원본 배열 요소들의 순서를 반대로 정렬            |                          |
  | push & pop      | 배열의 가장 뒤에 요소를 추가 & 제거              |                          |
  | unshift & shift | 배열의 가장 앞에 요소를 추가 & 제거              |                          |
  | includes        | 배열에 특정 값이 존재하는지 판별 후 참/거짓 반환 |                          |
  | indexOf         | 배열에 특정 값이 존재하는지 판별 후 인덱스 반환  | 요소가 없을 경우 -1 반환 |
  | join            | 배열의 모든 요소를 구분자를 이용하여 연결        | 구분자 생략 시 쉼표 기준 |

- 주요 메소드 - 심화 (Array Helper Methods)

  | 메소드  | 설명                                                        | 비고         |
  | ------- | ----------------------------------------------------------- | ------------ |
  | forEach | 배열의 각 요소에 콜백 함수를 한 번씩 실행                   | 반환 값 없음 |
  | map     | 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환          |              |
  | filter  | 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열 반환 |              |
  | reduce  | 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환       |              |
  | find    | 콜백 함수의 반환 값이 참이면 해당 요소를 반환               |              |
  | some    | 배열의 요소 중 하나라도 판별 함수를 통과하면 참을 반환      |              |
  | every   | 배열의 모든 요소가 판별 함수를 통과하면 참을 반환           |              |

  - 배열을 순회하며 특정 로직을 수행하는 메소드
  - 메소드 호출 시 인자로 callback 함수를 받는 것이 특징

#### reverse

```javascript
const numbers = [1, 2, 3, 4, 5]
numbers.reverse()
console.log(numbers) // [5, 4, 3, 2, 1]
```

- **array.reverse()**
  - 원본 배열 요소들의 순서를 반대로 정렬

#### push & pop

```javascript
const numbers = [1, 2, 3, 4, 5]

numbers.push(100)
console.log(numbers) // [1, 2, 3, 4, 5, 100]

numbers.pop()
console.log(numbers) // [1, 2, 3, 4, 5]
```

- **array.push(value)**
  - 배열의 가장 뒤에 요소 추가
- **array.pop()**
  - 배열의 마지막 요소 제거

#### unshift & shift

```javascript
const numbers = [1, 2, 3, 4, 5]

numbers.unshift(100)
console.log(numbers) // [100, 1, 2, 3, 4, 5]

numbers.shift()
console.log(numbers) // [1, 2, 3, 4, 5]
```

- **array.unshift(value)**
  - 배열의 가장 앞에 요소 추가
- **array.shift()**
  - 배열의 첫 번째 요소 제거

#### includes

```javascript
const numbers = [1, 2, 3, 4, 5]

console.log(numbers.includes(1)) // true
console.log(numbers.includes(6)) // false
```

- **array.includes(value)**
  - 배열에 특정 값이 존재하는지 판별 후 참 또는 거짓 반환

#### indexOf

```javascript
const numbers = [1, 2, 3, 4, 5]
let result

result = numbers.indexOf(3)
console.log(result) // 2

result = numbers.indexOf(6)
console.log(result) // -1
```

- **array.indexOf(value)**
  - 배열에 특정 값이 존재하는지 확인 후 가장 첫 번째로 찾은 요소의 인덱스 반환
  - 만약 해당 값이 없을 경우 -1 반환

#### join

```javascript
const numbers = [1, 2, 3, 4, 5]
let result

result = numbers.join()
console.log(result) // 1,2,3,4,5

result = numbers.join('')
console.log(result) // 12345

result = numbers.join(' ')
console.log(result) // 1 2 3 4 5

result = numbers.join('-')
console.log(result) // 1-2-3-4-5
```

- **array.join([separator])**
  - 배열의 모든 요소를 연결하여 반환
  - separator(구분자)는 선택적으로 지정 가능하며, 생략 시 쉼표를 기본 값으로 사용

#### Spread operator

```javascript
const array = [1, 2, 3]
const newArray = [0, ...array, 4]

console.log(newArray) // [0, 1, 2, 3, 4]
```

- spread operator(…)를 사용하면 배열 내부에서 배열 전개 가능
  - (ES5까지는 Array.concat() 메서드를 사용했었음)
- 얕은 복사에 활용 가능

#### forEach

```javascript
array.forEach((element, index, array) => {
    // do something
})
```

```javascript
const fruits = ['딸기', '수박', '사과', '체리']

fruits.forEach((fruit, index, array) => {
  console.log(fruit, index, array)
  // 딸기 0 ['딸기', '수박', '사과', '체리']
  // 수박 1 ['딸기', '수박', '사과', '체리']
  // 사과 2 ['딸기', '수박', '사과', '체리']
  // 체리 3 ['딸기', '수박', '사과', '체리']
})
```

- **array.forEach(callback(element[, index[,array]]))**
  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
  - 콜백 함수는 3가지 매개변수로 구성
    - element: 배열의 요소
    - index: 배열 요소의 인덱스
    - array: 배열 자체
  - 반환 값(return)이 없는 메소드

#### map

```javascript
array.map((element, index, array) => {
    // do something
})
```

```javascript
const numbers = [1, 2, 3, 4, 5]

const doubleNums = numbers.map((num) => {
    return num * 2
})

console.log(doubleNums) // [2, 4, 6, 8, 10]
```

- **array.map(callback(element[, index[, array]]))**
  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
  - 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환
  - 기존 배열 전체를 다른 형태로 바꿀 때 유용

#### filter

```javascript
array.filter((element, index, array) => {
    // do something
})
```

```javascript
const numbers = [1, 2, 3, 4, 5]

const oddNums = numbers.filter((num, index) => {
    return num % 2
})

console.log(oddNums) // [1, 3, 5]
```

- **array.filter(callback(element[, index[, array]]))**
  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
  - 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환
  - 기존 배열의 요소들을 필터링할 때 유용

#### reduce

```javascript
array.reduce((acc, element, index, array) => {
    // do something
}, initialValue)
```

```javascript
const numbers = [1, 2, 3]

const result = numbers.reduce((acc, num) => {
    return acc + num
}, 0)

console.log(result) // 6
```

- **array.reduce(callback(acc, element, [index[, array]])[, initialValue])**
  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
  - 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환
  - reduce 메소드의 주요 매개변수
    -  acc : 이전 callback 함수의 반환 값이 누적되는 변수
    - initialValue(optional) : 최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫 번째 값
  - 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생

#### find

```javascript
array.find((element, index, array) => {
    // do something
})
```

```javascript
const avengers = [
    {name: 'Tony Stark', age: 45},
    {name: 'Steve Rogers', age: 32},
    {name: 'Thor', age: 40}
]

const result = avengers.find((avenger) => {
    return avenger.name === 'Tony Stark'
})

console.log(result) // {name: 'Tony Stark', age: 45}
```

- **array.find(callback(element[, index[, array]]))**
  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
  - 콜백 함수의 반환 값이 참이면, 조건을 만족하는 첫 번째 요소를 반환
  - 찾는 값이 배열에 없으면 undefined 반환

#### some

```javascript
array.some((element, index, array) => {
    // do something
})
```

```javascript
const numbers = [1, 3, 5, 7, 9]

const hasEvenNumber = numbers.some((num) => {
    return num % 2 === 0
})
console.log(hasEvenNumber) // false

const hasOddNumber = numbers.some((num) => {
    return num % 2
})
console.log(hasOddNumber) // true
```

- **array.some(callback(element[, index[, array]]))**
  - 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 참을 반환
  - 모든 요소가 통과하지 못하면 거짓 반환
  - 빈 배열은 항상 거짓 반환

#### every

```javascript
array.every((element, index, array) => {
    // do something
})
```

```javascript
const numbers = [2, 4, 6, 8, 10]

const isEveryNumberEven = numbers.every((num) => {
    return num % 2 === 0
})
console.log(isEveryNumberEven) // true

const isEveryNumberOdd = numbers.every((num) => {
    return num % 2
})
console.log(isEveryNumberOdd) // false
```

- **array.every(callback(element[, index[, array]]))**
  - 배열의 모든 요소가 주어진 판별 함수를 통과하면 참을 반환
  - 하나의 요소라도 통과하지 못하면 거짓 반환
  - 빈 배열은 항상 참 반환

### 객체 (Objects)

#### 객체 정의와 특징

```javascript
const me = {
  name: 'jack',
  phoneNumber: '01012345678',
  'samsung products': {
    buds: 'Galaxy Buds pro',
    galaxy: 'Galaxy s20’
  }
}

console.log(me.name)
console.log(me.phoneNumber)
console.log(me['samsung products'])
console.log(me['samsung products'].buds)
```

- 객체는 속성(property)의 집합이며,  중괄호 내부에 key와 value의 쌍으로 표현
- key는 문자열 타입만 가능
  - key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
- value는 모든 타입 (함수 포함) 가능
- 객체 요소 접근은 점 또는 대괄호로 가능
  - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

```javascript
const me = {
  firstName: 'John',
  lastName: 'Doe’,
  getFullName: function () {
    return this.firstName + this.lastName
  }
}
```

- 메소드는 객체의 속성이 참조하는 함수
- 객체.메소드명() 으로 호출 가능
- 메소드 내부에서는 this 키워드가 객체를 의미함

#### 객체 관련 ES6 문법

- ES6에 새로 도입된 문법들로 객체 생성 및 조작에 유용하게 사용 가능
  - 속성명 축약
  - 메소드명 축약
  - 계산된 속성명 사용하기
  - 구조 분해 할당
    - 구조 분해 할당은 [배열도 가능](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#%EB%B0%B0%EC%97%B4_%EA%B5%AC%EC%A1%B0_%EB%B6%84%ED%95%B4)
  - 객체 전개 구문(Spread Operator)

#### JSON

- [JavaScript Object Notation](https://www.ecma-international.org/publications-and-standards/standards/ecma-404/)
- key-value쌍의 형태로 데이터를 표기하는 언어 독립적 표준 포맷
- 자바스크립트의 객체와 유사하게 생겼으나 실제로는 문자열 타입
  - 따라서 JS의 객체로서 조작하기 위해서는 구문 분석(parsing)이 필수
- 자바스크립트에서는 JSON을 조작하기 위한 두 가지 내장 메소드를 제공
  - **JSON.parse()**
    - JSON => 자바스크립트 객체
  - **JSON.stringify()**
    - 자바스크립트 객체 => JSON


## 참고 사이트

- MDN 문서를 활용한 문법 학습
  - [JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/JavaScript)
  - [JavaScript - 동적인 클라이언트 사이드 스크립트 언어 - Web 개발 학습하기 | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Learn/JavaScript)
  - [JavaScript 안내서 - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide)

- 변수 선언
  - [문법과 자료형 - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#변수_선언)
- 배열
  - [Array - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array)
  - [Array.prototype.map() - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
  - [Array.prototype.forEach() - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
- 객체
  - [JavaScript 객체 기본 - Web 개발 학습하기 | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Objects/Basics)
- JSON
  - [JSON으로 작업하기 - Web 개발 학습하기 | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Objects/JSON)
- 함수
  - [함수 — 코드 재사용 - Web 개발 학습하기 | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Building_blocks/Functions)
- 화살표 함수
  - [화살표 함수 - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
- (심화) 함수와 화살표 함수의 차이
  - [this - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/this)
- (심화) 이벤트
  - [EventTarget.addEventListener() - Web API | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/API/EventTarget/addEventListener)
  - [함수 만들기 - Web 개발 학습하기 | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Building_blocks/Build_your_own_function)


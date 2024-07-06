# COMPUTER

- Calculation + Remember

  (계산기 + 기억 장치)

# Programming

- 명령어의 집합

# Python

- 인터프리터 언어 : 컴파일 과정 없이 한 줄 입력하고 실행한 후, 바로 확인 가능
- 객체 지향 언어 : 모든 것이 객체(숫자, 문자, 클래스 등 값을 가지고 있는 모든 것)로 구현되어 있음

## 기초 문법

- 코드는 위에서 아래로, 오른쪽에서 왼쪽으로

### 들여쓰기

- 문장 구분 용도
- 스페이스 4칸(권장 사항) 또는 탭 1칸
- **절대 혼용하지 말 것!**

### 변수

- 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름

- 참조하는 객체가 언제든 바뀔 수 있기 때문에 **변수**라고 불림

- 할당 연산자(=)를 통해 값을 할당

- type() :  할당된 값의 타입 확인

- id() : 객체 메모리주소 확인

  ```python
  i = 5
  j = 3
  s = '파이썬'
  
  type(i) 
  # int
  id(i) 
  # 4645387184
  i + j 
  # 8
  i - j 
  # 2
  j = -2
  i * j 
  # -10
  '안녕' + s 
  # 안녕파이썬
  s * 3 
  # 파이썬파이썬파이썬
  s = 'Python'
  s + ' is fun' 
  # Python is fun
  ```

- 같은 값을 동시에 할당 가능

  ```python
  x = y = 1004
  ```
  
- 다른 값을 동시에 할당 가능

  ```python
  x, y = 1, 2
  ```
  

### 식별자

- 파이썬 객체를 식별하기 위해 사용하는 이름

- 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성

- 첫 글자로 숫자는 불가능

- 길이 제한 없음, 대소문자 구별

- 다음의 키워드는 예약어로 사용할 수 없음
  ```python
  ['False', 'None', 'True', 'and', 'as', 'assert',  'async', 'await', 'break', 'class', 'continue',  'def', 'del', 'elif', 'else', 'except',  'finally', 'for', 'from', 'global', 'if',  'import', 'in', 'is', 'lambda', 'nonlocal',  'not', 'or', 'pass', 'raise', 'return', 'try',  'while', 'with', 'yield']
  ```

- 내장된 함수나 모듈 등의 이름으로도 만들면 안됨

### 사용자 입력

```python
input([prompt])
```

- 사용자로부터 값을 입력 받을 수 있는 내장 함수

- 대괄호 부분에 문자열을 넣으면 입력 시 해당 문자열을 출력할 수 있음

- 반환값은 항상 **문자열**의 형태

  ```python
  name = input('이름을 입력해주세요 : ')
  print(name)
  # 이름을 입력해주세요 : 파이썬
  type(name)
  # str
  ```

### 주석

- 코드에 대한 설명
  - 중요한 점이나 다시 확인해야 하는 부분을 #을 사용해 표시
  - 컴퓨터는 주석을 인식하지 않음

- 개발자에게 주석을 작성하는 습관은 **매우** 중요

## 파이썬 기본 자료형

### None

- 값이 없음을 표현하기 위한 타입
- 일반적으로 반환 값이 없는 함수에서 사용하기도 함

### 불린(Boolean)

- True / False 값을 가진 타입은 bool

- 비교 / 논리 연산을 수행하는 데 활용됨

- 다음은 모두 False로 변환

  ```python
  0, 0.0, (), [], {}, '', None
  ```

- bool() : 특정 데이터가 True인지 False인지 검증

#### 논리 연산자(and, or, not) : 논리식을 판단하여 True / False를 반환함

  | 연산자  |                       내용                       |
  | :-----: | :----------------------------------------------: |
  | A and B | A와 B 모두 True이면 True, 하나라도 False면 False |
  | A or B  | A와 B 하나라도 True이면 True, 모두 False면 False |
  |  not A  |       A가 True면  False, A가 False면 True        |

### 수치형

#### 정수(int)

- 모든 정수는 int
- 매우 큰 수를 나타낼 때도 오버플로우가 발생하지 않음

#### 실수(float)

- 정수가 아닌 모든 실수는 float

- 부동소수점

  - 실수를 컴퓨터가 표현하는 방법 - 2진수(비트)로 숫자를 표현

  - 이 과정에서 floating point rounding error가 발생하여 예상치 못한 결과가 나올 수 있음

    ```python
    3.14 - 3.02
    # 0.1200000000000001
    ```
#### 복소수(complex)

- 실수부와 허수부 j로 구성된 복소수는 모두 complex

  ```python
  a = 3+4j
  type(a)
  # <class 'complex'>
  a.real
  # 3.0
  a.imag
  # 4.0
  # 대충 이런게 있다~ 정도
  ```

#### 산술 연산자

| 연산자 |   내용   |
| :----: | :------: |
|   +    |   덧셈   |
|   -    |   뺄셈   |
|   *    |   곱셈   |
|   %    |  나머지  |
|   /    |  나눗셈  |
|   //   |    몫    |
|   **   | 거듭제곱 |

#### 복합 연산자

| 연산자  |    내용    |
| :-----: | :--------: |
| a += b  | a = a + b  |
| a -= b  | a = a - b  |
| a *= b  | a = a * b  |
| a /= b  | a = a / b  |
| a //= b | a = a // b |
| a %= b  | a = a % b  |
| a **= b | a = a ** b |

#### 비교 연산자

| 연산자 |            내용             |
| :----: | :-------------------------: |
|   <    |            미만             |
|   <=   |            이하             |
|   >    |            초과             |
|   >=   |            이상             |
|   ==   |            같음             |
|   !=   |          같지 않음          |
|   is   |    객체 아이덴티티(OOP)     |
| is not | 객체 아이덴디티가 아닌 경우 |

### 문자열(string)

```python
print('hello')
# hello
print(type('hello'))
# <class 'str'>

print("문자열 안에 '작은 따옴표'를 사용하려면 큰 따옴표로 묶는다.")
print('문자열 안에 "큰 따옴표"를 사용하려면 작은 따옴표로 묶는다.')
print('''문자열 안에 '작은 따옴표'나
"큰 따옴표"를 사용할 수 있고
여러 줄을 사용할 때도 편리하다.''')

# 슬라이싱
s = 'abcdefghi'
#    012345678
# (-)987654321 

print(s[1]) 
# b
print(s[2:5]) 
# cde
print(s[2:5:2])
# ce
print(s[5:2:-1])
# fed
print(s[:3])
# abc
print(s[5:])
# fghi
print(s[:])
# abcdefghi
print(s[::-1])
# ihgfedcba

# 결합
hello, ' + 'python!'
# 'hello, python!'

# 반복
hi!' * 3
# 'hi!hi!hi!'

# 포함
'a' in 'apple'
# True
'app' in 'apple'
# True
'b' in 'apple'
# False

# Escape sequence
print('철수 \'안녕\'')
# 철수 '안녕'
print('이 다음은 엔터.\n그리고 탭\t탭')
# 이 다음은 엔터.
# 그리고 탭 탭

# %-formatting
name = 'Kim'
score = 4.5
print('Hello, %s' % name)
print('내 성적은 %d' % score)
print('내 성적은 %f' % score)
# Hello, Kim
# 내 성적은 4
# 내 성적은 4.500000

# f-string
name = 'Kim'
score = 4.5
print(f'Hello, {name}! 성적은 {score}')
# Hello, Kim! 성적은 4.5
pi = 3.141592
print(f'원주율은 {pi:.3}. 반지름이 2일때 원의 넓이는 {pi*2*2}')
# '원주율은 3.14. 반지름이 2일때 원의 넓이는 12.566368'

# Immutable : 변경 불가능함
a = 'my string?'
a[-1] = ‘!’
TypeError Traceback (most recent call last) 
----> 1 a[-1] = '!’ 
TypeError: 'str' object does not support item assignment

# Iterable : 반복 가능함
a = '123'
for char in a:
print(char)
```
- 모든 문자는 str
- 작은 따옴표나 큰 따옴표를 활용하여 표기
  - 문자열을 묶을 때 동일한 문장 부호를 활용
  - 하나의 문장 부호를 선택하여 유지할 것

### 형 변환

- 파이썬에서 데이터 형태는 서로 변환할 수 있음

#### 암시적 형 변환

-  사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환 하는 경우

  ```python
  True + 3
  # 4
  3 + 5.0
  # 8.0
  3 + 4j + 5
  # (8+4j)
  ```


#### 명시적 형 변환

- 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환 하는 경우

  ```python
  # 문자열은 암시적 타입 변환이 되지 않음
  '3' + 4
  # TypeError: can only concatenate str (not "int") to str
  # 명시적 타입 변환이 필요함
  int('3') + 4
  # 7
  # 정수 형식이 아닌 경우 타입 변환할 수 없음
  int('3.5') + 5
  # ValueError: invalid literal for int() with base 10: '3.5'
  float('3.5') + 5
  # 8.5
  # 형식에 맞는 문자열만 가능
  ```

## 컨테이너

- 여러 개의 값을 담을 수 있는 객체로, 서로 다른 자료형을 저장할 수 있음
- 순서가 있는 데이터 vs 순서가 없는 데이터
- 순서가 있다 != 정렬되어 있다
- 시퀀스
  - 문자열 : 문자들의 나열
  - 리스트 : 변경 가능한 값들의 나열
  - 튜플 : 변경 불가능한 값들의 나열
  - 레인지 : 숫자의 나열

- 컬렉션(비시퀀스)
  - 세트 : 유일한 값들의 모음
  - 딕셔너리 : 키-값들의 모음

- 시퀀스형 주요 공통 연산자

  |       연산       |                          결과                           |
  | :--------------: | :-----------------------------------------------------: |
  |       s[i]       |               s의 i번째 항목, 0에서 시작                |
  |      s[i:j]      |               s의 i에서 j까지의 슬라이스                |
  |     s[i:j:k]     |            s의 i에서 j까지 스텝 k의 슬라이스            |
  |      s + t       |                   s와 t를 이어붙이기                    |
  | s * n 또는 n * s |                s를 그 자신에 n번 더하기                 |
  |      x in s      | s의 항목 중 하나가 x와 같으면 True, 그렇지 않으면 False |
  |    x not in s    | s의 항목 중 하나가 x와 같으면 False, 그렇지 않으면 True |
  |      len(s)      |                        s의 길이                         |
  |      min(s)      |                   s의 가장 작은 항목                    |
  |      max(s)      |                    s의 가장 큰 항목                     |

### 리스트

- 변경 가능한 값들이 나열된 자료형

- 순서를 가지며, 서로 다른 타입의 객체를 가질 수 있음

- 변경 가능하며, 반복 가능함

- 항상 대괄호 형태로 정의하며, 객체는 콤마로 구분

- 대괄호([]) 혹은 list()를 통해 생성

- 순서가 있는 시퀀스로 인덱스를 통해 접근 가능(list[i])

  ```python
  # 생성
  my_list = []
  another_list = list()
  type(my_list)
  # <class 'list'>
  type(another_list)
  # <class 'list'>
  
  # 값 접근
  a = [1, 2, 3]
  print(a[0])
  # 1
  # 값 변경
  a[0] = '1'
  print(a)
  # ['1', 2, 3]
  
  # 값 추가
  even_numbers = [2, 4, 6, 8]
  even_numbers.append(10)
  even_numbers
  # => [2, 4, 6, 8, 10]
  
  # 값 삭제
  even_numbers = [2, 4, 6, 8]
  even_numbers.pop(0)
  even_numbers
  # => [4, 6, 8]
  
  boxes = ['apple', 'banana']
  len(boxes)
  # 2
  boxes[1]
  # 'banana'
  boxes[1][0]
  # 'b'
  ```

### 튜플

- 불변한 값들의 나열

- 순서를 가지며, 서로 다른 타입의 객체를 가질 수 있음

- 변경 불가능하며, 반복 가능함

- 항상 소괄호 형태로 정의하며, 요소는 콤마로 구분

- 소괄호(()) 혹은 tuple()을 통해 생성

- 값에 대한 접근은 리스트와 동일하게 인덱스로 접근

  ```python
  # 값 접근
  a = (1, 2, 3, 1)
  a[1]
  
  # 값 변경 => 불가능
  a[1] = ‘3’
  
  TypeError Traceback (most recent call last) 
  1 # 값 변경 => 불가능 ----> 
  2 a[1] = '3’ 
  TypeError: 'tuple' object does not support item assignment
  
  ```

### 레인지

- 숫자의 시퀀스를 나타내기 위해 사용
  - range(n) : 0부터 n-1까지의 숫자
  - range(n, m) : n부터 m-1까지의 숫자
  - range(n, m, s) : n부터 m-1까지 s만큼 증가
- 변경 불가능하며 반복 가능함

  ```python
  range(4)
  # range(0, 4)
  list(range(4))
  # [0, 1, 2, 3]
  # 담겨있는 숫자를 확인하기 위하여 리스트로 형변환
  # 실제 활용시에는 형변환 필요 없음
  type(range(4))
  # <class 'range'>
  
  # 0부터 특정 숫자까지
  list(range(3))
  # [0, 1, 2]
  
  # 숫자의 범위
  list(range(1, 5))
  # [1, 2, 3, 4]
  
  # step 활용
  list(range(1, 5, 2))
  # [1, 3]
  
  # 역순
  list(range(6, 1, -1))
  # [6, 5, 4, 3, 2]
  
  list(range(6, 1, 1))
  # []
  ```

### 세트

- 유일한 값들의 모음
- 순서가 없고, 중복된 값이 없음
  - 집합과 동일한 구조를 가지며, 집합 연산도 가능

- 변경 가능하며, 반복 가능함
  - 단, 세트는 순서가 없어서 반복의 결과가 정의한 순서와 다를 수 있음

- 중괄호({}) 혹은 set()를 통해 생성
  - 빈 set를 만들기 위해선 반드시 set() 활용

- 순서가 없으므로 인덱스 접근 불가능

  ```python
  {1, 2, 3, 1, 2}
  # {1, 2, 3}
  type({1, 2, 3})
  # <class 'set'>
  blank_set = set()
  
  {'hi', 1, 2}
  # => {1, 2, 'hi'}
  
  {1, 2, 3}[0]
  TypeError Traceback (most recent call last) 
  <ipython-input-95-0c8fa4a2ff15> in <module> 
  ----> 1 {1, 2, 3}[0] 
  TypeError: 'set' object is not subscriptable
  
  # 값 추가
  numbers = {1, 2, 3}
  numbers.add(5)
  numbers
  # => {1, 2, 3, 5}
  numbers.add(1)
  numbers
  # => {1, 2, 3, 5}
  
  # 값 삭제
  numbers = {1, 2, 3}
  numbers.remove(1)
  numbers
  # => {2, 3}
  numbers.remove(5)
  # Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
  #KeyError: 5
  
  # 중복된 값 제거
  my_list = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산’]
  len(set(my_list))
  # 4
  ```
### 딕셔너리

- 키 - 값 쌍으로 이루어진 모음
  - 키 : 불변 자료형(string, integer, float, boolean, tuple, range)만 가능 (리스트, 딕셔너리 등은 불가능함)
  - 값 : 모든 값으로 설정 가능

- 키와 값은 : 으로 구분되고 개별 요소는 콤마로 구분됨
- 변경 가능하며 반복 가능함
  - 딕셔너리는 반복하면 키가 반환됨
  ```python
  students = {'홍길동': 30, '김철수': 25}
  students['홍길동']
  # 30
  
  dict_c = {[1, 2, 3]: 'hi’}
  TypeError Traceback (most recent call last) 
  ----> 1 dict_c = {[1, 2, 3]: 'hi’} 
  TypeError: unhashable type: 'list'
                    
  movie = {
  'title': '설국열차', 
  'genres': ['SF', '액션', '드라마'],
  'open_date': '2013-08-01',
  'time': 126,
  'adult': False, 
  }
  movie['genres']
  # ['SF', '액션', '드라마']
  # 없는 키                  
  movie['actors’]
  Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  KeyError: 'actors'
        
  # 키-값 추가 및 변경
  students = {'홍길동': 100, '김철수': 90}
  students['홍길동'] = 80
  # {'홍길동': 80, '김철수': 90}
  students['박영희'] = 95
  # {'홍길동': 80, '김철수': 90, '박영희': 95}
  
  # 키 삭제
  students = {'홍길동': 30, '김철수': 25}
  students.pop('홍길동')
  students
  # {'김철수': 25}
  ```

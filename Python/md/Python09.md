# 파이썬 응용 심화

## Comprehension

- 표현식과 제어문을 통해 특정한 값을 가진 자료를 간결하게 생성하는 방법

- List Comprehension

  `[<expression> for <var> in <iterable>]`

  `[<expression> for <var> in <iterable> if <conditional>]`

  ```python
  cubic_list = [number**3 for number in range(1, 4)] # 1~3의 세제곱의 결과가 담긴 리스트
  even_list = [number for number in range(1, 11) if number % 2 == 0] # 1부터 10까지의 자연수 중 짝수만
  ```

- Dictionary Comprehension

  `{key : value for <var> in <iterable>}`

  `{key : value for <var> in <iterable> if <conditional>}`

  ```python
  cubic_dict = {number : number**3 for number in range(1, 4)} # 1~3의 세제곱의 결과가 담긴 딕셔너리
  ```



## map

- 순회 가능한 데이터 구조의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환

- `map(function, iterable)`

  ```python
  def mul_2(n) :
      return n * 2
  numbers = [1, 2, 3]
  result = map(mul_2, numbers)
  print(list(result), type(result))
  # [2, 4, 6] <class 'map'>
  ```

  

## filter

- 순회 가능한 데이터 구조의 모든 요소에 함수를 적용하고, 그 결과가 True인 것들을 filter object로 반환

- `filter(function, iterable)`

  ```python
  def odd(n) :
      return n % 2
  numbers = [1, 2, 3]
  result = filter(odd, numbers)
  print(list(result), type(result))
  # [1, 3] <class 'filter'>
  ```

  

## lambda

- 표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수여서 **익명함수**라고도 불림
- `lambda [parameter] : <expression>`

- 특징
  - return문을 가질 수 없음
  - 간편 조건문 외 다른 조건문이나 반복문을 가질 수 없음
- 장점
  - 함수를 정의해서 사용하는 것보다 간결함
  - def를 사용할 수 없는 곳에서도 사용 가능함 

  ```python
  n = [1, 2, 5, 10, 3, 9, 12]
  print(list(filter(lambda i: i % 3 == 0, n)))
  # [3, 9, 12]
  print(list(map(lambda i: i * 3, n)))
  # [3, 6, 15, 30, 9, 27, 36]
  ```



## 어노테이션

- 단순 메모로서 사용법에 대한 힌트를 제공

  - 동적 타입 언어인 파이썬을 정적 타입으로 확정시켜주는 것이 아님

- 변수 어노테이션

  ```python
  a: int
  a = 3
  print(a, type(a))
  # 3 <class 'int'>
  a = 'a'
  print(a, type(a))
  # a <class 'str'>
  ```

- 함수 어노테이션

  ```python
  def add(x: int, y: int) -> int :
      return x + y
  print(add(7, 4))
  # 11
  print(add('hi', 'hello'))
  # hihello
  ```

  

# 파이썬 버전별 업데이트

## 모듈 심화

- [파이썬 표준 라이브러리](https://docs.python.org/ko/3/library/index.html) : 파이썬에 기본적으로 설치된 모듈과 내장 함수

- 파이썬 패키지 관리자(pip) : PyPI에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템

- 패키지 설치

  - 최신 버전 / 특정 버전 / 최소 버전을 명시하여 설치 가능
  - 이미 설치되어 있는 경우 알림을 띄우고 아무것도 하지 않음

- 패키지 활용 명령어

  ```bash
  $ pip install SomePackage # SomePackage 설치
  $ pip install SomePackage==1.0.5 # SomePackage 버전 1.0.5 설치
  $ pip install 'SomePackage>=1.0.4'
  $ pip uninstall SomePackage # SomePackage 제거
  $ pip list # 패키지 목록 확인
  $ pip show SomePackage # 특정 패키지 정보 확인
  $ pip freeze > requirements.txt # 패키지 목록 내보내기
  $ pip install -r requirement.txt # 패키지 목록 일괄 설치
  $ pip install --upgrade pip # pip 버전 업그레이드
  ```
  
  

## 가상 환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치해야 함
- 여러 프로젝트를 하는 경우 버전이 서로 다를 수 있음
- 이러한 경우 가상 환경을 만들어 프로젝트별로 독립적인 패키지를 관리할 수 있음

### venv

- 가상 환경을 만들고 관리하는데 사용되는 모듈

- 특정 폴더에 가상 환경을 만들고, 고유한 패키지 집합을 가질 수 있음

  - 특정 폴더에 가상 환경(패키지 집합 폴더)이 있고 
  - bash같은 실행 환경에서 활성화 시키면
  - 해당 폴더에 있는 패키지를 관리 및 사용 가능

- 가상 환경을 생성하면 해당 폴더에 별도의 파이썬 패키지가 설치됨

  ```bash
  $ python -m venv <folder_name>
  ```

- 가상 환경 활성화 (`<venv>`는 가상 환경을 포함하는 폴더의 이름)

  | 플랫폼  | 셸              | 명령어                                |
  | ------- | --------------- | ------------------------------------- |
  | POSIX   | bash/zsh        | `$ source <venv> /bin/activate`       |
  |         | fish            | `$ source <venv> /bin/activate.fish`  |
  |         | csh/tcsh        | `$ source <venv> /bin/activate.csh`   |
  |         | PowerShell Core | `$ <venv> /bin/Activate.ps1`          |
  | Windows | cmd.exe         | `C:\> <venv>\Scripts\activate.bat`    |
  |         | PowerShell      | `PS C:\> <venv>\Scripts\Activate.ps1` |

- 가상 환경 비활성화

  `$ deactivate`


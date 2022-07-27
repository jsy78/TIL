# CRUD

- **Create, Read, Update, Delete**
  - 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능

# 문자열

- 문자열은 **iterable**(순회 가능), **immutable**(변경 불가능)한 자료형

  ```python
  # 문자열은 변경 불가능하지만 변경 가능한 것처럼 조작할 수 있음
  word = "apple"
  print(word)
  print(id(word))
  >>> apple
  >>> 1352749370800
  
  word += " banana"
  print(word)
  print(id(word))
  >>> apple banana
  >>> 1352749417520
  
  # 하지만 위와 같이 apple banana 라는 문자열을 새로 만든 것일 뿐 실제로 더해진 것은 아님
  # 추가된 데이터로 인해 word 기존의 'apple' 은 찾을 수 없음
  ```

- 슬라이싱

  | 문자열 |  a   |  b   |  c   |  d   |  e   |  f   |  g   |  h   |  i   |
  | :----: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
  | index  |  0   |  1   |  2   |  3   |  4   |  5   |  6   |  7   |  8   |
  | index  |  -9  |  -8  |  -7  |  -6  |  -5  |  -4  |  -3  |  -2  |  -1  |

  ```python
  # 양수 인덱스 - 문자열 길이 == 음수 인덱스
  # 기본
  s[2:5] # 'cde'
  s[-6:-2] # 'defg'
  # 스텝
  s[2:5:2] # 'ce'
  s[-6:-1:3] # 'dg'
  # 역방향 스텝
  s[2:5:-1] # ''
  s[5:2:-1] # 'fed'
  # 처음부터
  s[:3] # 'abc'
  # 끝까지
  s[5:] # 'fghi'
  # 거꾸로
  s[::-1] # 'ihgfedcba'
  ```

- 문자열 메소드

  | 메소드                           | 설명                                                         |
  | :------------------------------- | ------------------------------------------------------------ |
  | .split(기준 문자)                | 문자열을 일정 기준으로 **나누어 리스트로 변환**<br/>괄호 안에 값을 넣지 않으면 **공백**을 기준으로 설정 |
  | .strip(제거할 문자)              | 문자열의 양쪽 끝에 있는 **특정 문자를 모두 제거한 새로운 문자열 반환**<br/>괄호 안에 값을 넣지 않으면 **공백**을 제거 문자로 설정<br/>제거할 문자를 여러 개 넣으면 해당하는 모든 문자들을 제거 |
  | .find(찾는 문자)                 | 특정 문자가 **처음**으로 나타나는 **위치(인덱스)를 반환**<br/>찾을 문자가 없다면 `-1` 반환 |
  | .index(찾는 문자)                | 특정 문자가 **처음**으로 나타나는 **위치(인덱스)를 반환**<br/>찾을 문자가 없다면 ***오류*** 발생 |
  | .count(개수를 셀 문자)           | 문자열에서 **특정 문자가 몇 개인지 반환**<br/>문자 뿐만 아니라, 문자열의 개수도 확인 가능 |
  | .replace(기존 문자, 새로운 문자) | 문자열에서 **기존 문자를 새로운 문자로 수정**한 새로운 문자열 반환<br/>특정 문자를 빈 문자열('')로 수정하여 마치 해당 문자를 삭제한 것 같은 효과 가능 |
  | 삽입할 문자.join(iterable)       | iterable의 **각각 원소 사이에 특정 문자를 삽입**한 새로운 문자열 반환<br/>공백 출력, 콤마 출력 등 원하는 출력 형태를 위해 사용 |

  ```python
  word = "I play the piano"
  print(word.split())
  # ['I', 'play', 'the', 'piano']
  
  word = "Hello Worlddddddd"
  print(word.strip("d")) # Hello Worl
  print(word.strip("Hd")) # ello Worl
  
  word = "apple"
  print(word.find("p")) # 1
  print(word.find("k") # -1
  
  word = "apple"
  print(word.find("p")) # 1
  print(word.find("k")
  # ValueError : substring not found
        
  word = "banana"
  print(word.count("a")) # 3
  print(word.count("na")) # 2
  print(word.count("ana")) # 1
        
  word = "happyhacking"
  print(word.replace("happy", "angry")) # angryhacking
  print(word.replace("h", "H")) # HappyHacking
  print(word.replace("happy", " ")) # hacking
           
  word = "happyhacking"
  print(" ".join(word)) # h a p p y h a c k i n g
  print(",".join(word)) # h,a,p,p,y,h,a,c,k,i,n,g
  
  word2 = ["edu", "hphk.kr"]
  print("@".join(word)) # edu@hphk.kr
  
  word3 = ["h", "a", "p", "p", "y"]
  print("".join(words)) # happy
  ```

## ASCII

![img](https://github.com/Jobyeongjin/TIL/raw/master/git-start.assets/ascii.png)

- **American Standard Code for Information Interchange**

  - 미국 정보 교환 표준 부호

- 알파벳을 표현하는 대표 인코딩 방식

- 각 문자를 표현하는데 1 byte(8 bits) 사용

  - 1 bit : 통신 에러 검출용
  - 7 bit : 문자 정보 저장(총 2^7 = 128개)

- 관련 내장함수

  | 함수            | 설명                     |
  | --------------- | ------------------------ |
  | ord(문자)       | 문자를 아스키코드로 변환 |
  | chr(아스키코드) | 아스키코드를 문자로 변환 |

  ```python
  print(ord("A")) # 65
  print(ord("a")) # 97
  
  print(char(65)) # A
  print(char(97)) # a
  ```

  

# 딕셔너리

- 파이썬에 내장된 자료구조
- 순서가 없고, 키-값 쌍으로 접근
  - 키 값은 변경 불가능
- 정식 이름은 **해시 테이블**
  - **해시 함수** : 임의 길이의 데이터를 고정 길이의 데이터로 대응시키는 함수
  - **해시** : 해시 함수를 통해 얻어진 값

- 삽입, 삭제, 수정, 조회 연산 속도가 리스트보다 빠름

  - 산술 계산으로 값이 있는 위치를 바로 알 수 있기 때문

  | 연산 종류   | 딕셔너리 | 리스트       |
  | ----------- | -------- | ------------ |
  | Get item    | O(1)     | O(1)         |
  | Insert item | O(1)     | O(1) or O(N) |
  | Update item | O(1)     | O(1)         |
  | Delete item | O(1)     | O(1) or O(N) |
  | Search item | O(1)     | O(N)         |

## 딕셔너리는 언제 사용할까?

- 리스트를 사용하기 힘든 경우
- 데이터에 대한 빠른 접근 탐색이 필요한 경우
  - 현실 세계 대부분의 데이터를 다룰 경우

## 딕셔너리 기본 문법

`var = {key1 : value1, key2 : value2}`

```python
# 생성
a = {
  "name": "kyle"
  "gender": "male"
  "address": "Seoul"
}

# 조회
print(a["name"]) # 딕셔너리[key]
print(a.get("name")) # 딕셔너리.get(key) 값이 없으면 None 반환 

# 삽입
a['job'] = 'coach'

# 수정
# 내부에 해당 key가 없으면 삽입, 있으면 수정
a["name"] = "justin"

# 삭제
# 내부에 존재하는 키에 대한 값 삭제 및 반환, 존재하지 않는 키라면 KeyError 발생
# default 값을 지정하여 KeyError 방지 가능
gender = a.pop("gender")
print(gender, a)
# male {'name': 'kyle', 'address': 'Seoul'}
phone = a.pop("phone")
# keyError
phone = a.pop("phone", 0)
# 0
```

```python
# 카운팅
def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

countLetters('hello world')
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# collections 모듈 내장 함수 Counter 활용
from collections import Counter

Counter('hello world') 
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
Counter('hello world').most_common() 
# [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
Counter('hello world').most_common(1) 
# [('l', 3)]
```

## 딕셔너리 메소드

| 메소드    | 설명                                             |
| --------- | ------------------------------------------------ |
| .keys()   | **Key** 목록이 담긴 dict_keys 객체 반환          |
| .values() | **Value** 목록이 담긴 dict_values 객체 반환      |
| .items()  | **Key, Value** 목록이 담긴 dict_values 객체 반환 |

```python
a = {
  "name": "kyle"
  "gender": "male"
  "address": "Seoul"
}
print(a.keys())
# dict_keys(['name', 'gender', 'address'])
print(a.values())
# dict_values(['kyle', 'male', 'seoul'])
print(a.items())
# dict_items([('name', 'kyle') ('gender', 'male'), ('address', 'seoul')])
```


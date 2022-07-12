# 제어문

## 조건문

-  특정 상황에 따라 코드를 선택적으로

- 참/거짓을 판단할 수 있는 조건식과 함께 사용

- ```python
  if < expression >:
  	# Run this Code block
  else:
  	# Run this Code block
  ```

### 복수 조건문

- 복수의 조건식을 활용할 경우 elif를 활용하여 표현함

- ```python
  if <expression>:
  	# Code block
  elif <expression>:
  	# Code block
  elif <expression>:
  	# Code block
  else:
  	# Code block
  ```

### 중첩 조건문

- 조건문은 다른 조건문에 중첩되어 사용될 수 있음 (들여쓰기에 유의할 것)

- ```python
  if <expression>:
  	# Code block
  	if <expression>:
  		# Code block
  else:
  	# Code block
  ```

### 조건 표현식

- 일반적으로 조건에 따라 값을 할당할 때 활용

- ```python
  <true인 경우 값> if <expression> else <false인 경우 값>
  
  value = num if num >= 0 else -num # 절댓값 저장
  result = '홀' if num % 2 else '짝' # 홀짝 판별
  ```

## 반복문

- 특정 조건에 도달할 때까지 계속 반복되는 구문
- while :  종료 조건에 해당하는 코드를 통해 종료시켜야 함

- for : 반복 가능한 객체를 모두 순회하면 종료 (별도의 종료 조건이 필요 없음)

- 반복 제어 : break, continue, for-else

### while

- while문은 조건식이 참인 경우 반복적으로 코드를 실행

- 조건식이 참인 경우 들여쓰기 되어 있는 코드 블록이 실행됨

- 코드 블록이 모두 실행되면 다시 조건식을 검사하여 반복 실행

- 무한 루프에 빠지지 않도록 종료 조건을 확실히 명시할 것

- ```python
  while <expression> :
      # code block
  ```
### for

- 문자열, tuple, list, range, dictionary, enumerate같은 시퀀스를 포함한 순회 가능한 객체(iterable)의 요소를 모두 순회함

- ```python
  for <변수명> in <iterable>:
  	# Code block
  ```

- enumerate() : 인덱스와 객체를 쌍으로 담은 열거형 객체를 반환

  - (index, value) 형태의  tuple로 구성된 열거 객체를 반환

  - ```python
    members = ['민수', '영희', '철수']
    for i in range(len(members)):
        print(f’{i} {members[i]}')
    
    for i, member in enumerate(members):
        print(i, member)
              
    list(enumerate(members))
    # [(0, '민수'), (1, '영희'), (2, '철수')]
    list(enumerate(members, start=1))
    # [(1, '민수'), (2, '영희'), (3, '철수')
    ```

- dictionary는 기본적으로 key를 순회하며, key를 통해 값을 활용

  - ```python
    grades = {'john': 80, 'eric': 90}
    for name in grades:
    	print(name)
    # john 
    # eric  
    
    grades = {'john': 80, 'eric': 90}
    for name in grades:
    	print(name, grades[name])
    # john 80 
    # eric 90
    ```

### 반복문 제어

- break : break문을 만나면 반복문은 종료됨

  - ```python
    n = 0
    while True:
    	if n == 3:
    		break
    	print(n)
    	n += 1
    # 0
    # 1
    # 2
    ```

- continue :  continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

  - ```python
    for i in range(6):
        if i % 2 == 0:
            continue
        print(i)
    # 1
    # 3
    # 5
    ```

- for-else

  - ```python
    for char in 'apple':
    	if char == 'b':
    		print('b!')
    		break
    else:
    	print('b가 없습니다.')
    # b가 없습니다.
    ```

  - ```python
    for char in 'banana':
    	if char == 'b':
    		print('b!')
    		break
    else:
    print('b가 없습니다.')
    # b!
    ```
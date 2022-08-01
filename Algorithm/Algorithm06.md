# 스택

## 스택의 개념

- 데이터를 한 쪽에서만 넣고 빼는 자료구조
- 가장 마지막에 들어온 데이터가 가장 먼저 나가므로 **LIFO(Last-in First-out, 후입선출) 방식**

## 스택의 대표 동작

- push : 스택에 새로운 데이터를 삽입하는 행위
- pop : 스택의 가장 마지막 데이터를 빼오는 행위
- 파이썬은 list로 스택을 간편하게 구현 가능함
  - push : `.append`()
  - pop : `.pop()`

## 스택을 쓰는 이유

- 뒤집기, 되돌리기, 되돌아가기 
  - 뒤로 가기 버튼
  - Ctrl + Z
  - 브라우저 히스토리
  - 단어 뒤집기
- 마무리 되지 않은 일을 임시 저장

## 스택 활용 예시

- 괄호 매칭

  ```python
  map(int, input().split()) # 정상
  map(int, input().split())) # 괄호가 잘못 들어갔다고 알림
  ```

  - 열린 괄호가 스택에 들어오고 그 이후 닫힌 괄호가 들어오면 완료
  - 열렸는데 닫히지 않은 것들을 찾음

- 함수 호출 (재귀 호출)

  ```python
  print(sum(max(min(2, 5), 10), min(2, 5)))
  >>> print(sum(max(2, 10), min(2, 5)))
  >>> print(sum(10, min(2, 5)))
  >>> print(sum(10, 2))
  >>> print(12)
  >>> 12
  ```

- 백트래킹
- DFS (깊이 우선 탐색)

# 큐

## 큐의 개념

- 한 쪽 끝에서 데이터를 넣고, 다른 한 쪽에서만 데이터를 뺄 수 있는 자료구조
- 가장 먼저 들어온 데이터가 먼저 나가므로 **FIFO (First-in First-out, 선입선출) 방식**

## 큐의 대표 동작

- enqueue : 맨 뒤에 데이터를 삽입하는 행위
- dequeue : 맨 앞 데이터를 가져오는 행위
- 파이썬은 list로 큐를 간편하게 구현 가능함
  - enqueue : `.append()`
  - dequeue  : `.pop(0)`
  - 데이터를 뺄 때 큐 안에 있는 데이터가 많은 경우 비효율적
    - 맨 앞 데이터가 빠지면서, 리스트의 인덱스가 하나씩 당겨지기 때문
  - append()와 pop()은 O(1) 이지만 pop(0)의 경우 O(n)
    - 이러한 연산이 빈번하게 이루어지면 속도가 느려질 가능성이 높음
    - 따라서 이런 경우엔 덱을 활용하는 것이 효율적

## 덱의 개념

- 큐 자료구조의 단점을 보완한 자료구조
- 양방향으로 삽입과 삭제가 자유로움
- 삽입과 추출이 모두 큐보다 훨씬 빠름

## 덱의 대표 동작

- append: 맨 뒤[-1]에 데이터를 삽입하는 행위
- pop: 맨 뒤[-1] 데이터를 가져오는 행위
- appendleft: 맨 앞[0]에 데이터를 삽입하는 행위
- popleft: 맨 앞[0] 데이터를 가져오는 행위

## 큐와 덱의 활용 예시

```python
from collections import deque

# 큐 활용 예시
n = int(input())
queue = list(range(1, n + 1))

while len(queue) > 1:
  print(queue.pop(0), end=' ')
  queue.append(queue.pop(0))

print(queue[0])


# 덱 활용 예시 1
n = int(input())
queue = deque(range(1, n + 1))

while len(queue) > 1:
  print(queue.popleft(), end=' ')
  queue.append(queue.popleft())

print(queue[0])

# 덱 활용 예시 2
numbers = [1, 2, 3, 4, 5]

queue = deque(numbers)

queue.append(6)

queue.popleft()

print(queue)
>>> deque([2, 3, 4, 5, 6])

# 리스트 형태로 출력
print(list(queue))
>>> [2, 3, 4, 5, 6]

# 하나씩 출력
for num in queue:
  print(num, end=' ')
>>> 2 3 4 5 6
```


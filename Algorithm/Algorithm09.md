# 2차원

## 순회

- 2차원 리스트를 단순히 print한 결과

  ```python
  matrix = [
  	[1, 2, 3, 4],
  	[5, 6, 7, 8],
  	[9, 0, 1, 2]
  ]
  
  print(matrix)
  >>> [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]]
  ```

- 인덱스를 통해 각각 출력한 결과

  ```python
  matrix = [
  	[1, 2, 3, 4],
  	[5, 6, 7, 8],
  	[9, 0, 1, 2]
  ]
  
  print(matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3])
  print(matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3])
  print(matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3])
  
  >>> 1 2 3 4
  >>> 5 6 7 8
  >>> 9 0 1 2
  # 하지만 리스트의 크기가 커지면 이 방법은 쓸 수 없음
  ```

- 이중 for문을 이용한 **행 우선 순회**

  ```python
  matrix = [
  	[1, 2, 3, 4],
  	[5, 6, 7, 8],    # 가로로 이동한다
  	[9, 0, 1, 2]
  ]
  
  for i in range(3):
  	for j in range(4):
  		print(matrix[i][j], end=" ") # 하나의 행을 출력
  	print()
     
  >>> 1 2 3 4
  >>> 5 6 7 8
  >>> 9 0 1 2
  ```

  | 행(`i`) | 열(`j`) | `matrix[i][j]` |
  | :-----: | :-----: | :------------: |
  |    0    |    0    |       1        |
  |    0    |    1    |       2        |
  |    0    |    2    |       3        |
  |    0    |    3    |       4        |
  |    1    |    0    |       5        |
  |    1    |    1    |       6        |
  |    1    |    2    |       7        |
  |    1    |    3    |       8        |
  |    2    |    0    |       9        |
  |    2    |    1    |       0        |
  |    2    |    2    |       1        |
  |    2    |    3    |       2        |

- 이중 for문을 이용한 **열 우선 순회**

  ```python
  matrix = [
  	[1, 2, 3, 4],
  	[5, 6, 7, 8],    # 세로로 내려간다
  	[9, 0, 1, 2]
  ]
  
  for i in range(4):
  	for j in range(3):
  		print(matrix[j][i], end=" ") # 하나의 열을 출력
  	print()
     
  >>> 1 5 9
  >>> 2 6 0
  >>> 3 7 1
  >>> 4 8 2
  ```

  | 열(`i`) | 행(`j`) | `matrix[i][j]` |
  | :-----: | :-----: | :------------: |
  |    0    |    0    |       1        |
  |    0    |    1    |       5        |
  |    0    |    2    |       9        |
  |    1    |    0    |       2        |
  |    1    |    1    |       6        |
  |    1    |    2    |       0        |
  |    2    |    0    |       3        |
  |    2    |    1    |       7        |
  |    2    |    2    |       1        |
  |    3    |    0    |       4        |
  |    3    |    1    |       8        |
  |    3    |    2    |       2        |

- 행 우선 순회를 이용해 이차원 리스트의 총합 구하기

  ```python
  matrix = [
  	[1, 1, 1, 1],
  	[1, 1, 1, 1],
  	[1, 1, 1, 1]
  ]
  
  total = 0
  
  for i in range(3):
  	for j in range(4):
  		total += matrix[i][j]
  
  print(total)
  >>> 12
  ```

- Pythonic한 방법으로 이차원 리스트의 총합 구하기

  ```python
  matrix = [
  	[1, 1, 1, 1],
  	[1, 1, 1, 1],
  	[1, 1, 1, 1]
  ]
  
  total = sum(map(sum, matrix))
  
  print(total)
  >>> 12
  ```

- 행 우선 순회를 이용해 이차원 리스트의 최댓값, 최솟값 구하기

  ```python
  matrix = [
  	[0, 5, 3, 1],
  	[4, 6, 10, 8],
  	[9, -1, 1, 5]
  ]
  
  max_value = 0
  min_value = 99999999
  
  # 최댓값
  for i in range(3):
  	for j in range(4):
  		if matrix[i][j] > max_value:
  			max_value = matrix[i][j]
             
  print(max_value)
  >>> 10
  
  # 최솟값
  for i in range(3):
  	for j in range(4):
  		if matrix[i][j] < min_value:
  			min_value = matrix[i][j]
  
  print(min_value)
  >>> -1
  ```

- Pythonic한 방법으로 이차원 리스트의 최댓값, 최솟값 구하기

  ```python
  matrix = [
  	[0, 5, 3, 1],
  	[4, 6, 10, 8],
  	[9, -1, 1, 5]
  ]
  
  max_value = max(map(max, matrix))
  min_value = min(map(min, matrix))
  
  print(max_value)
  >>> 10
  
  print(min_value)
  >>> -1
  ```

- 예제

  > 2행 3열 리스트 두 개에 각각의 값을 입력 받은 후 두 배열의 같은 위치끼리 곱하여 새로운 리스트에
  > 저장한 후 출력하는 프로그램을 작성하시오. 
  
  ```python
  list_a = [list(map(int, input().split())) for i in range(2)]
  list_b = [list(map(int, input().split())) for i in range(2)]
  list_c = [[0] * 3 for _ in range(2)]
  
  # 두 배열의 같은 위치끼리 곱하여 새로운 이차원 리스트에 저장
  for i in range(2):
  	for j in range(3):
  		list_c[i][j] = list_a[i][j] * list_b[i][j]
  
  # 결과 출력
  for i in range(2):
  	for j in range(3):
  		print(list_c[i][j], end=" ")
  	print()
  ```
  
  


## 전치

- 전치(transpose)란 행렬의 행과 열을 서로 맞바꾸는 것을 의미함

  |       | **0** | **1** | **2** | **3** |
  | :---: | :---: | :---: | :---: | :---: |
  | **0** |   1   |   2   |   3   |   4   |
  | **1** |   5   |   6   |   7   |   8   |
  | **2** |   9   |   0   |   1   |   2   |

  |       | **0** | **1** | **2** |
  | :---: | :---: | :---: | :---: |
  | **0** |   1   |   5   |   9   |
  | **1** |   2   |   6   |   0   |
  | **2** |   3   |   7   |   1   |
  | **3** |   4   |   8   |   2   |
  
  ```python
  matrix = [
  	[1, 2, 3, 4],
  	[5, 6, 7, 8],
  	[9, 0, 1, 2]
  ]
  
  transposed_matrix = [[0] * 3 for _ in range(4)] # 전치 행렬을 담을 이차원 리스트 초기화
  											    # (행과 열의 크기가 반대)
  for i in range(4):
  	for j in range(3):
  		transposed_matrix[i][j] = matrix[j][i] # 행, 열 맞바꾸기
  
  # transposed_matrix = [[matrix[j][i] for j in range(3)] for i in range(4)]
  # transposed_matrix = list(map(list, zip(*matrix)))
  
  """
  transposed_matrix = [
  	[1, 5, 9], 
  	[2, 6, 0], 
  	[3, 7, 1], 
  	[4, 8, 2]
  ]
  """
  ```
  
  

## 회전

- 문제에서 이차원 리스트를 왼쪽, 오른쪽으로 90도씩 회전하는 경우가 존재함

  (원본)

  |       |     **0**      |  **1**   |  **2**   |
  | :---: | :------------: | :------: | :------: |
  | **0** | ***1*** (0, 0) | 2 (0, 1) | 3 (0, 2) |
  | **1** |    4 (1, 0)    | 5 (1, 1) | 6 (1, 2) |
  | **2** |    7 (2, 0)    | 8 (2, 1) | 9 (2, 2) |

  (왼쪽으로 90도 회전 == 오른쪽으로 270도 회전) : (i, j) ← (j, n-1-i)

  |       |          **0**          |       **1**       |       **2**       |
  | :---: | :---------------------: | :---------------: | :---------------: |
  | **0** |    3 (0, 0) ← (0, 2)    | 6 (0, 1) ← (1, 2) | 9 (0, 2) ← (2, 2) |
  | **1** |    2 (1, 0) ← (0, 1)    | 5 (1, 1) ← (1, 1) | 8 (1, 2) ← (2, 1) |
  | **2** | ***1*** (2, 0) ← (0, 0) | 4 (2, 1) ← (1, 0) | 7 (2, 2) ← (2, 0) |

  (왼쪽으로 180도 회전 == 오른쪽으로 180도 회전) : (i, j) ← (n-1-i, n-1-j)

  |       |       **0**       |       **1**       |          **2**          |
  | :---: | :---------------: | :---------------: | :---------------------: |
  | **0** | 9 (0, 0) ← (2, 2) | 8 (0, 1) ← (2, 1) |    7 (0, 2) ← (2, 0)    |
  | **1** | 6 (1, 0) ← (1, 2) | 5 (1, 1) ← (1, 1) |    4 (1, 2) ← (1, 0)    |
  | **2** | 3 (2, 0) ← (0, 2) | 2 (2, 1) ← (0, 1) | ***1*** (2, 2) ← (0, 0) |

  (왼쪽으로 270도 회전 == 오른쪽으로 90도 회전) : (i, j) ← (n-1-j, i)

  |       |       **0**        |       **1**       |          **2**          |
  | :---: | :----------------: | :---------------: | :---------------------: |
  | **0** | 7 (0, 0) ← (2, 0)  | 4 (0, 1) ← (1, 0) | ***1*** (0, 2) ← (0, 0) |
  | **1** | 8 (1, 0) ← (2, 1)  | 5 (1, 1) ← (1, 1) |    2 (1, 2) ← (0, 1)    |
  | **2** | 9  (2, 0) ← (2, 2) | 6 (2, 1) ← (1, 2) |    3 (2, 2) ← (0, 2)    |

- 코드 구현

  ```python
  matrix = [
  	[1, 2, 3],
  	[4, 5, 6],
  	[7, 8, 9]
  ]
  
  n = 3
  rotated_matrix = [[0] * n for _ in range(n)]
  
  for i in range(n):
  	for j in range(n):
  		rotated_matrix[i][j] = matrix[j][n-1-i] # 왼쪽으로 90도 회전하기 (오른쪽으로 270도 회전하기)
  
  # rotated_matrix = [[matrix[j][n-1-i] for j in range(n)] for i in range(n)]    
  # rotated_matrix = list(map(list, zip(*matrix)))[::-1]
  
  """
  rotated_matrix = [
  	[3, 6, 9],
  	[2, 5, 8],
  	[1, 4, 7]
  ]
  """
  ```
  ```python
  matrix = [
  	[1, 2, 3],
  	[4, 5, 6],
  	[7, 8, 9]
  ]
  
  n = 3
  rotated_matrix = [[0] * n for _ in range(n)]
  
  for i in range(n):
  	for j in range(n):
  		rotated_matrix[i][j] = matrix[n-1-i][n-1-j] # 왼쪽으로 180도 회전하기 (오른쪽으로 180도 회전하기)
     
  # rotated_matrix = [[matrix[n-1-i][n-1-j] for j in range(n)] for i in range(n)]    
  
  """
  rotated_matrix = [
  	[9, 8, 7],
  	[6, 5, 4],
  	[3, 2, 1]
  ]
  """
  ```
  ```python
  matrix = [
  	[1, 2, 3],
  	[4, 5, 6],
  	[7, 8, 9]
  ]
  
  n = 3
  rotated_matrix = [[0] * n for _ in range(n)]
  
  for i in range(n):
  	for j in range(n):
  		rotated_matrix[i][j] = matrix[n-1-j][i] # 왼쪽으로 270도 회전하기 (오른쪽으로 90도 회전하기)
     
  # rotated_matrix = [[matrix[n-1-j][i] for j in range(n)] for i in range(n)]    
  # rotated_matrix = list(map(list, zip(*matrix[::-1])))
  
  """
  rotated_matrix = [
  	[7, 4, 1],
  	[8, 5, 2],
  	[9, 6, 3]
  ]
  """
  ```
  
  

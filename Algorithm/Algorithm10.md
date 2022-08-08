# 완전탐색

## 브루트 포스

- Brute-force는 모든 경우의 수를 탐색하여 문제를 해결하는 방식
- 가장 단순한 풀이 기법이며, 단순 조건문과 반복문을 이용
- 복잡한 알고리즘 보다는, 아이디어를 어떻게 코드로 구현할 것인지가 중요함

### [2798번: 블랙잭 (acmicpc.net)](https://www.acmicpc.net/problem/2798)

> N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

| 입력                   | 출력 |
| ---------------------- | ---- |
| `5 21`<br/>`5 6 7 8 9` | `21` |

```python
def blackjack(n, m, cards):
    max_total = 0 # 현재 가장 큰 합
    # 완전탐색(Brute-force)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                total = cards[i] + cards[j] + cards[k]
                
                # 현재 가장 큰 합보다는 크고, m을 넘지 않아야 갱신
                if max_total < total <= m:
                max_total = total
                
                # 합과 m이 같으면 더 이상 탐색하는 의미가 없으므로 종료
                if total == m:
                    return total
    return max_total
```



## 델타 탐색

- (0, 0)부터 이차원 리스트의 모든 원소를 순회하며 각 지점에서 **상하좌우에 위치한 다른 지점을 조회하거나 이동**하는 방식

- 이차원 리스트의 인덱스(좌표) 조작을 통해서 상하좌우 탐색을 수행함

  - 이때 행과 열의 변화량인 -1, +1을 **델타(delta)**값이라 함

    ```python
    # 1-1. 행을 x, 열을 y로 표현하여 델타값 정의 (상하좌우)
    dx = [-1, 1,  0, 0]
    dy = [ 0, 0, -1, 1]
    #      ↑, ↓,  ←, →  
    
    # 1-2. 행을 r, 열을 c로 표현하여 델타값 정의 (상하좌우)
    dr = [-1, 1,  0, 0]
    dc = [ 0, 0, -1, 1]
    #      ↑, ↓,  ←, →  
    
    # 상 (x-1, y)
    nx = x + dx[0]
    ny = y + dy[0]
    
    # 하 (x+1, y)
    nx = x + dx[1]
    ny = y + dy[1]
    
    # 좌 (x, y-1)
    nx = x + dx[2]
    ny = y + dy[2]
    
    # 우 (x, y+1)
    nx = x + dx[3]
    ny = y + dy[3]
    
    # 2.이차원 리스트 순회
    for x in range(n):
        for y in range(m):
    
            # 3. 델타값을 이용해 상하좌우 이동
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
        
                # 4. 범위를 벗어나지 않으면 갱신
                if 0 <= nx < max_row and 0 <= ny < max_col:
                    x = nx
                    y = ny
    ```

    ```python
    # 상, 하, 좌, 우, 좌상, 좌하, 우상, 우하
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]
    ```

    

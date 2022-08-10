# 그래프 탐색 알고리즘

- 시작 정점에서 간선을 타고 이동할 수 있는 모든 정점을 찾는 알고리즘
- 스택과 큐 자료구조의 개념을 함께 활용

## 깊이 우선 탐색 (DFS)

![depth-first-search-in-graph-data-structure](https://www.simplilearn.com/ice9/free_resources_article_thumb/Graph%20Data%20Structure%20-%20Soni/depth-first-search-in-graph-data-structure.png)

> 시작 정점으로부터 갈 수 있는 하위 정점까지 가장 깊게 탐색하고,  
>
> 더 이상 갈 곳이 없다면 마지막 갈림길로 돌아와서 다른 정점을 탐색하며 결국 모든 정점을 방문하는 순회 방법

- 그래프의 깊이를 우선으로 탐색
- **스택**의 개념을 활용
- 미로 탈출
  - 어느 한 쪽 길로 가장 깊게 들어갔다가 막히면 다시 돌아와서 다른 길을 탐색
- 모든 정점을 방문할 때 유리하므로 경우의 수, 순열과 조합 문제에서 많이 사용됨
- 너비 우선 탐색에 비해 코드 구현이 간단함

### DFS 동작 과정

1. 탐색을 진행할 그래프를 표현

   ![https://ibb.co/4fPn9rc](https://i.ibb.co/fS4zBwb/image.png)

   ```python
   # 인접 행렬
   graph = [
       [0, 1, 1, 0, 0, 0, 0],
       [1, 0, 0, 1, 1, 0, 0],
       [1, 0, 0, 0, 1, 1, 0],
       [0, 1, 0, 0, 0, 0, 0],
       [0, 1, 1, 0, 0, 0, 1],
       [0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0]
   ]
   
   # 인접 리스트
   graph = [
       [1, 2],
       [0, 3, 4],
       [0, 4, 5],
       [1],
       [1, 2, 6],
       [2],
       [4]
   ]
   ```

2. 정점 방문 여부를 판별할 체크 리스트 생성

   ```python
   visited = [False] * n # n은 정점의 개수
   ```

   |     `i`      |   `0`   |   `1`   |   `2`   |   `3`   |   `4`   |   `5`   |   `6`   |
   | :----------: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
   | `visited[i]` | `False` | `False` | `False` | `False` | `False` | `False` | `False` |


3. 현재 정점 방문 처리

4. 인접한 모든 정점 확인

5. 방문하지 않은 인접 정점 이동

   ```python
   def DFS(start):
       stack = [start] # 돌아갈 곳을 기록
       visited[start] = True # 시작 정점 방문 처리
   
       while stack: # 스택이 빌 때까지(돌아갈 곳이 없을때까지) 반복
           cur = stack.pop() # 현재 방문 정점(후입선출)
           if not visited[cur] : # 아직 방문하지 않았다면
               visited[cur] = True # 방문 처리
           
           for adj in graph[cur]: # 인접한 모든 정점에 대해
               if not visited[adj]: # 아직 방문하지 않았다면
                   stack.append(adj) # 스택에 넣기
                   
   DFS(0) # 0번 정점에서 시작                
   ```
   
   

## 너비 우선 탐색 (BFS)

![breadth-first-search-in-graph-data-structure](https://www.simplilearn.com/ice9/free_resources_article_thumb/Graph Data Structure - Soni/breadth-first-search-in-graph-data-structure.png)

- 그래프의 너비를 우선으로 탐색
- **큐**의 개념을 활용
- 모든 정점을 방문할 필요가 없거나 최단 거리를 구하는 경우 DFS보다 유리함

### BFS 동작 과정
1. 탐색을 진행할 그래프를 표현

   ![https://ibb.co/4fPn9rc](https://i.ibb.co/fS4zBwb/image.png)

   ```python
   # 인접 행렬
   graph = [
       [0, 1, 1, 0, 0, 0, 0],
       [1, 0, 0, 1, 1, 0, 0],
       [1, 0, 0, 0, 1, 1, 0],
       [0, 1, 0, 0, 0, 0, 0],
       [0, 1, 1, 0, 0, 0, 1],
       [0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0]
   ]
   
   # 인접 리스트
   graph = [
       [1, 2],
       [0, 3, 4],
       [0, 4, 5],
       [1],
       [1, 2, 6],
       [2],
       [4]
   ]
   ```

2. 정점 방문 여부를 판별할 체크 리스트 생성

   ```python
   visited = [False] * n # n은 정점의 개수
   ```

   |     `i`      |   `0`   |   `1`   |   `2`   |   `3`   |   `4`   |   `5`   |   `6`   |
   | :----------: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: | :-----: |
   | `visited[i]` | `False` | `False` | `False` | `False` | `False` | `False` | `False` |


3. 현재 정점 방문 처리

4. 인접한 모든 정점 확인

5. 방문하지 않은 인접 정점 이동

   ```python
   from collections import deque
   
   def BFS(start):
       queue = deque([start]) # 돌아갈 곳을 기록
       visited[start] = True # 시작 정점 방문 처리
   
       while queue: # 큐가 빌 때까지(돌아갈 곳이 없을때까지) 반복
           cur = queue.popleft() # 현재 방문 정점(선입선출)
           if not visited[cur]: # 아직 방문하지 않았다면
               visited[cur] = True # 방문 처리
           
           for adj in graph[cur]: # 인접한 모든 정점에 대해
               if not visited[adj]: # 아직 방문하지 않았다면
                   queue.append(adj) # 큐에 넣기
                   
   BFS(0) # 0번 정점에서 시작                
   ```
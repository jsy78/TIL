## 후기 작성
마지막 알고리즘 수업이라니 아쉽다...
### 반반
문자열의 각 문자의 count가 전부 2면 조건을 만족한다.
### 모음이 보이지 않는 사람
그냥 replace 5번... 파이썬 갓갓
### 퍼펙트 셔플
카드 수가 홀수일 때와 짝수일 때를 나눠서 풀었다. 
슬라이싱을 통해 카드 덱을 반으로 나눠서 순서대로 추가해줬다.
### Flatten
리스트의 최댓값을 1 빼고 최솟값을 1 더한다. 
이걸 주어진 덤프 횟수만큼 반복한다.
### 창용 마을 무리의 개수
[백준 11724 연결 요소의 개수](https://www.acmicpc.net/problem/11724)와 동일한 문제였다.
### 등산로 조성
스택을 사용한 반복문으로 풀려고 시도했으나
visit 백트래킹 과정에 막혀서 결국 익숙하지도 않은 재귀를 시도해야만 했다.

```python
def DFS_construction(r, c, limit, length) : # 현재 위치 좌표, 공사 가능 횟수, 현재 길이
    global max_length
    # visited[r][c] == 1 코드 다시 확인해보니까 이렇게 쓰여있었음... 어이없는 실수
    visited[r][c] = 1
    
    for dr, dc in delta :
        .
        .
        if mountain[nr][nc] < mountain[r][c] : # 다음 위치의 원래 높이가 기존 위치의 높이보다 낮음
            DFS_construction(nr, nc, limit, length+1) # 다음 위치 좌표 및 높이, 공사 안 함, 길이 증가
        .
        .
        .
    max_length = max(max_length, length) # 길이 갱신
    
    # visited[r][c] == 0 코드 다시 확인해보니까 이렇게 쓰여있었음... 어이없는 실수
    visited[r][c] = 0

T = int(input())
for test_case in range(1, T+1) :
    .
    .
    .
    for i in range(N) :
        for j in range(N) :
            if mountain[i][j] == high_len :           
                DFS_construction(i, j, 1, 1) # 현재 위치 좌표, 공사 가능 횟수, 현재 길이
    .            
    .            
```
처음엔 이렇게 함수의 처음과 끝에서 visit 백트래킹을 시도했고 정답이 나왔다.
```python
def DFS_construction(r, c, limit, length) : # 현재 위치 좌표, 공사 가능 횟수, 현재 길이
    .
    .
    .
            visited[nr][nc] = 1 # 방문
            DFS_construction(nr, nc, limit, length+1) # 다음 위치 좌표 및 높이, 공사 안 함, 길이 증가
            visited[nr][nc] = 0 # 끝자락에 도달했으면 역순으로 되돌아가면서 방문 해제
       .
       .
       .
                if mountain[nr][nc] < mountain[r][c] : # 깎은 높이가 기존 높이보다 낮아지면
                    visited[nr][nc] = 1 # 방문
                    DFS_construction(nr, nc, limit-1, length+1) # 다음 위치 좌표 및 높이, 공사함, 길이 증가   
                    visited[nr][nc] = 0 # 끝자락에 도달했으면 역순으로 되돌아가면서 방문 해제
                
                .
                .
T = int(input())
for test_case in range(1, T+1) :
    .
    .
    .
    for i in range(N) :
        for j in range(N) :
            if mountain[i][j] == high_len :           
                visited[i][j] = 1 # 맨 처음 위치 방문
                DFS_construction(i, j, 1, 1) # 현재 위치 좌표, 공사 가능 횟수, 현재 길이
                visited[i][j] = 0 # 모든 호출이 끝나고 마지막으로 처음 위치 방문 해제
    .
    .
```
이렇게 해도 되긴 했다.

```python
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

def DFS_construction(r, c, h, limit, length) : # 현재 위치 좌표 및 높이, 공사 가능 횟수, 현재 등산로 길이
    global max_length
    .
    .
    .   
    for dr, dc in delta :
        nr, nc = r + dr, c + dc # 다음 위치 좌표
        .
        .
        nh = mountain[nr][nc] # 다음 위치의 높이
        if nh < h : # 다음 위치의 원래 높이가 기존 위치의 높이보다 낮음 
            DFS_construction(nr, nc, nh, limit, length+1) # 다음 위치 좌표 및 높이, 공사 안 함, 길이 증가  
        elif nh >= h and limit > 0 : # 다음 위치의 원래 높이가 기존 위치보다 높거나 같고 공사 가능 횟수 남음
            for i in range(1, K+1) :
                nh -= i # 다음 위치의 높이를 정수 단위로 최대 K만큼 깎음
                if nh < h : # 깎은 높이가 기존 높이보다 낮아지면
                    DFS_construction(nr, nc, nh, limit-1, length+1) # 다음 위치 좌표 및 높이, 공사함, 길이 증가   
                
    .
    .
    .

T = int(input())
for test_case in range(1, T+1) :
    .
    .

    for i in range(N) :
        for j in range(N) :
            if mountain[i][j] == high_len :           
                DFS_construction(i, j, mountain[i][j], 1, 1)
    .
    .
               
```

그리고 `nh`라는 변수를 만들어서 재귀 호출을 시도했으나 일부 테스트 케이스에서 오답을 도출했다.

```python
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

def DFS_construction(r, c, h, limit, length) : # 현재 위치 좌표 및 높이, 공사 가능 횟수, 현재 등산로 길이
    global max_length
    .
    .
    .   
    for dr, dc in delta :
        nr, nc = r + dr, c + dc # 다음 위치 좌표
        .
        .
        nh = mountain[nr][nc] # 다음 위치의 높이
        if nh < h : # 다음 위치의 원래 높이가 기존 위치의 높이보다 낮음 
            DFS_construction(nr, nc, nh, limit, length+1) # 다음 위치 좌표 및 높이, 공사 안 함, 길이 증가  
        elif nh >= h and limit > 0 : # 다음 위치의 원래 높이가 기존 위치보다 높거나 같고 공사 가능 횟수 남음
            for i in range(1, K+1) :
                nh -= i # 다음 위치의 높이를 정수 단위로 최대 K만큼 깎음
                if nh < h : # 깎은 높이가 기존 높이보다 낮아지면
                    DFS_construction(nr, nc, nh, limit-1, length+1) # 다음 위치 좌표 및 높이, 공사함, 길이 증가   
                nh += i # 다음 위치의 높이 복구
    .
    .
    .

T = int(input())
for test_case in range(1, T+1) :
    .
    .

    for i in range(N) :
        for j in range(N) :
            if mountain[i][j] == high_len :           
                DFS_construction(i, j, mountain[i][j], 1, 1)
    .
    .
               
```

알고 보니 `nh += i`라는 구문으로 직전 높이를 복구하는 과정이 빠져서 그랬던 거였다.

```python
def DFS_construction(r, c, limit, length) : # 현재 위치 좌표, 공사 가능 횟수, 현재 길이
    .
    .
    .
        
        if mountain[nr][nc] < mountain[r][c] : # 다음 위치의 원래 높이가 기존 위치의 높이보다 낮음 
            DFS_construction(nr, nc, limit, length+1) # 다음 위치 좌표 및 높이, 공사 안 함, 길이 증가
        
        elif mountain[nr][nc] >= mountain[r][c] and limit > 0 : 
            for i in range(1, K+1) :
                mountain[nr][nc] -= i # 다음 위치의 높이를 정수 단위로 최대 K만큼 깎음
                if mountain[nr][nc] < mountain[r][c] : # 깎은 높이가 기존 높이보다 낮아지면
                    DFS_construction(nr, nc, limit-1, length+1) # 다음 위치 좌표 및 높이, 공사함, 길이 증가   
                mountain[nr][nc] += i # 다음 위치의 높이 복구
    .
    .
    .

T = int(input())
for test_case in range(1, T+1) :
    .
    .

    for i in range(N) :
        for j in range(N) :
            if mountain[i][j] == high_len :           
                DFS_construction(i, j, 1, 1)
    .
    .
               
```

`nh` 변수 없이 직접 액세스해도 괜찮았다.

```python
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

def DFS_construction(r, c, limit, length) : # 현재 위치 좌표, 공사 가능 횟수, 현재 길이
    global max_length

    if visited[r][c] == 1 : # 현재 위치 방문 여부 체크
        return

    visited[r][c] = 1 # 현재 위치 방문

    for dr, dc in delta :
        nr, nc = r + dr, c + dc # 다음 위치 좌표
        
        if not (0 <= nr < N and 0 <= nc < N) : # 범위 체크
            continue
        
        if visited[nr][nc] == 1 : # 다음 위치의 방문 여부 체크
            continue
        
        if mountain[nr][nc] < mountain[r][c] : # 다음 위치의 원래 높이가 기존 위치의 높이보다 낮음 
            DFS_construction(nr, nc, limit, length+1) # 다음 위치 좌표 및 높이, 공사 안 함, 길이 증가
        
        elif mountain[nr][nc] >= mountain[r][c] and limit > 0 : # 다음 위치의 원래 높이가 기존 위치보다 높거나 같고 공사 가능 횟수 남음
            for i in range(1, K+1) :
                mountain[nr][nc] -= i # 다음 위치의 높이를 정수 단위로 최대 K만큼 깎음
                if mountain[nr][nc] < mountain[r][c] : # 깎은 높이가 기존 높이보다 낮아지면
                    DFS_construction(nr, nc, limit-1, length+1) # 다음 위치 좌표 및 높이, 공사함, 길이 증가   
                mountain[nr][nc] += i # 다음 위치의 높이 복구
    
    max_length = max(max_length, length) # 길이 갱신

    visited[r][c] = 0 # 끝자락에 도달했으면 역순으로 되돌아가면서 방문 해제

T = int(input())
for test_case in range(1, T+1) :
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    high_len = max(map(max, mountain))
    max_length = 0

    for i in range(N) :
        for j in range(N) :
            if mountain[i][j] == high_len :           
                DFS_construction(i, j, 1, 1)

    print(f'#{test_case} {max_length}')
```

최종 수정본


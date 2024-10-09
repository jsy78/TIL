import sys
from collections import deque
sys.stdin = open('1227_미로2.txt', 'r')

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
# def DFS(r, c) :
#     if visited[r][c] :
#         return
    
#     visited[r][c] = True

#     for dr, dc in delta :
#         nr, nc = r + dr, c + dc
#         if 0 <= nr < 100 and 0 <= nc < 100 :
#             if maze[nr][nc] != 1 and not visited[nr][nc] :
#                 DFS(nr, nc)
#     return

def BFS(r, c) :
    queue = deque()
    queue.append((r, c))

    while queue :
        qr, qc = queue.popleft()
        visited[qr][qc] = True
        for dr, dc in delta :
            nr, nc = qr + dr, qc + dc
            if 0 <= nr < 100 and 0 <= nc < 100 :
                if maze[nr][nc] != 1 and not visited[nr][nc] :
                    queue.append((nr, nc))
        

for test_case in range(1, 11) : 
    N = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    visited = [[False for _ in range(100)] for _ in range(100)]

    for i in range(100) :
        for j in range(100) :
            if maze[i][j] == 2 :
                BFS(i, j)
    
    for i in range(100) :
        for j in range(100) :
            if maze[i][j] == 3 :
                if visited[i][j] :
                    print(f'#{N} 1')
                else :
                    print(f'#{N} 0')
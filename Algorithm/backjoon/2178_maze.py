import sys
from collections import deque

sys.stdin = open('2178_maze.txt', 'r')

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]

dr = [-1, 1,  0, 0]
dc = [ 0, 0, -1, 1]

visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

# def DFS(r: int, c: int) -> None :
#     for k in range(4) :
#         nr = r + dr[k]
#         nc = c + dc[k]

#         if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == '1' :
#             if visited[nr][nc] == 0 or visited[nr][nc] > visited[r][c] + 1 :
#                 visited[nr][nc] = visited[r][c] + 1
#                 if nr == N-1 and nc == M-1 :
#                     return
#                 DFS(nr, nc)
#     return

# DFS(0, 0)
# print(visited[N-1][M-1])

def BFS(r: int, c: int) -> None :
    queue = deque()
    queue.append((r, c))

    while queue :
        i, j = queue.popleft()
        for k in range(4) :
            nr = i + dr[k]
            nc = j + dc[k]

            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == '1' :
                if visited[nr][nc] == 0 or visited[nr][nc] > visited[i][j] + 1 :
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[i][j] + 1
    
BFS(0, 0)
print(visited[N-1][M-1])
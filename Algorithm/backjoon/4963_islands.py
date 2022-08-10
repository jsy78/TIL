from sys import stdin
from collections import deque

stdin = open('4963_islands.txt', 'r')
input = stdin.readline

delta = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, 1), (1, -1), (-1, -1))

def DFS_recursive(r, c, w, h, area, visited) : # RecursionError 주의
    if visited[r][c] == 1 :
        return
    if area[r][c] == 0 :
        return
    visited[r][c] = 1
    for dr, dc in delta :
        nr = r + dr
        nc = c + dc
        if 0 <= nr < h and 0 <= nc < w :
            if visited[nr][nc] == 0 and area[nr][nc] == 1 : 
                DFS_recursive(nr, nc, w, h, area, visited)
    return

def DFS_iterative(r, c, w, h, area, visited) :
    stack = list()
    stack.append((r, c))
    while stack :
        pr, pc = stack.pop()
        if visited[pr][pc] == 0 and area[pr][pc] == 1 :
            visited[pr][pc] = 1
        for dr, dc in delta :
            nr = pr + dr
            nc = pc + dc
            if 0 <= nr < h and 0 <= nc < w :
                if visited[nr][nc] == 0 and area[nr][nc] == 1 :
                    stack.append((nr, nc))

def BFS(r, c, w, h, area, visited) :
    queue = deque()
    queue.append((r, c))
    while queue :
        pr, pc = queue.popleft()
        for dr, dc in delta :
            nr = pr + dr
            nc = pc + dc
            if 0 <= nr < h and 0 <= nc < w :
                if visited[nr][nc] == 0 and area[nr][nc] == 1 :
                    queue.append((nr, nc))
                    visited[nr][nc] = 1

while True :
    w, h = map(int, input().split())
    if w == 0 and h == 0 :
        break

    area = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]

    cnt = 0
    for i in range(h) :
        for j in range(w) :
            if visited[i][j] == 0 and area[i][j] == 1 :
                # DFS_recursive(i, j, w, h, area, visited)
                DFS_iterative(i, j, w, h, area, visited)
                # BFS(i, j, w, h, area, visited)
                cnt += 1
    print(cnt)


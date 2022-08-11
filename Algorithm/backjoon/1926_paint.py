from collections import deque
from sys import stdin
from pprint import pprint

stdin = open('1926_paint.txt', 'r')
input = stdin.readline

n, m = map(int, input().split())
paint = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
delta = ((0, 1), (1, 0), (-1, 0), (0, -1))

# def DFS_recursive(r, c) :
#     if visited[r][c] == 1 :
#         return
#     if paint[r][c] == 0 :
#         return
#     visited[r][c] = 1
#     for dr, dc in delta :
#         nr = r + dr
#         nc = c + dc
#         if 0 <= nr < n and 0 <= nc < m :
#             if visited[nr][nc] == 0 and paint[nr][nc] == 1 :
#                 DFS_recursive(nr, nc)
#     return

def DFS_iterative(r, c) :
    area = 0
    stack = list()
    stack.append((r, c))
    while stack :
        pr, pc = stack.pop()
        if visited[pr][pc] == 0 and paint[pr][pc] == 1 :
            visited[pr][pc] = 1
            area += 1
        for dr, dc in delta :
            nr = pr + dr
            nc = pc + dc
            if 0 <= nr < n and 0 <= nc < m :
                if visited[nr][nc] == 0 and paint[nr][nc] == 1 :
                    stack.append((nr, nc))
    return area

def BFS(r, c) :
    area = 0
    queue = deque()
    queue.append((r, c))
    while queue :
        pr, pc = queue.popleft()
        if visited[pr][pc] == 0 and paint[pr][pc] == 1 :
            visited[pr][pc] = 1
            area += 1
        for dr, dc in delta :
            nr = pr + dr
            nc = pc + dc
            if 0 <= nr < n and 0 <= nc < m :
                if visited[nr][nc] == 0 and paint[nr][nc] == 1 :
                    queue.append((nr, nc))
    return area

result = []
for i in range(n) :
    for j in range(m) :
        if visited[i][j] == 0 and paint[i][j] == 1 :
            # result.append(DFS_iterative(i, j))
            result.append(BFS(i, j))

pprint(paint)
pprint(visited)
print(result)
print(len(result))
print(max(result)) if len(result) != 0 else print(0)
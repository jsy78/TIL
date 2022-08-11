from collections import deque
from sys import stdin
from pprint import pprint

stdin = open('1926_paint.txt', 'r')
input = stdin.readline

def DFS_iterative(r, c) :
    paint[r][c] = 0
    area = 1
    delta = ((0, 1), (1, 0), (-1, 0), (0, -1))
    stack = list()
    stack.append((r, c))
    while stack :
        pr, pc = stack.pop()
        if paint[pr][pc] == 1 :
            paint[pr][pc] = 0
            area += 1    
        for dr, dc in delta :
            nr = pr + dr
            nc = pc + dc
            if 0 <= nr < n :
                if 0 <= nc < m :
                    if paint[nr][nc] == 1 :
                        stack.append((nr, nc))
    return area

def BFS(r, c) :
    area = 1
    paint[r][c] = 0
    delta = ((0, 1), (1, 0), (-1, 0), (0, -1))
    queue = deque()
    queue.append((r, c))
    while queue :
        pr, pc = queue.popleft()
        for dr, dc in delta :
            nr = pr + dr
            nc = pc + dc
            if 0 <= nr < n :
                if 0 <= nc < m :
                    if paint[nr][nc] == 1 :
                        paint[nr][nc] = 0
                        queue.append((nr, nc))
                        area += 1    
    return area

n, m = map(int, input().split())
paint = [list(map(int, input().split())) for _ in range(n)]
result = []
for i in range(n) :
    for j in range(m) :
        if paint[i][j] == 1 :
            # result.append(DFS_iterative(i, j))
            result.append(BFS(i, j))

pprint(paint)
print(result)
print(len(result))
print(max(result)) if len(result) != 0 else print(0)
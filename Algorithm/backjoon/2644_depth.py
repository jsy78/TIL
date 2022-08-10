from sys import stdin
from collections import deque

input = stdin.readline

V = int(input())
V1, V2 = map(int, input().split())
E = int(input())
adjacent_list = [[] for _ in range(V+1)]
visited = []
depth = [0 for _ in range(V+1)]

for _ in range(E) :
    v1, v2 = map(int, input().split())
    adjacent_list[v1].append(v2)
    adjacent_list[v2].append(v1)

def DFS_recursive(v) :
    visited.append(v)
    for n in adjacent_list[v] :
        if n not in visited :
            depth[n] = depth[v] + 1
            DFS_recursive(n)
    return

def DFS_iterative(v) :
    stack = list()
    stack.append(v)
    while stack :
        p = stack.pop()
        if p not in visited :
            visited.append(p)
        for n in adjacent_list[p] :
            if n not in visited :
                stack.append(n)
                depth[n] = depth[p] + 1           

def BFS(v) :
    queue = deque()
    queue.append(v)
    visited.append(v)
    while queue :
        p = queue.popleft()
        for n in adjacent_list[p] :
            if n not in visited :
                queue.append(n)
                visited.append(n)
                depth[n] = depth[p] + 1
            
DFS_iterative(V1)
#DFS_recursive(V1)
#BFS(V1)
print(depth[V2]) if depth[V2] != 0 else print(-1)
print(visited)
print(depth)
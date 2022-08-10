from sys import stdin
from collections import deque

input = stdin.readline

V, E = map(int, input().split())
adjacent_list = [[] for _ in range(V+1)]
visited = []
connected_component = []

for _ in range(E) :
    v1, v2 = map(int, input().split())
    adjacent_list[v1].append(v2)
    adjacent_list[v2].append(v1)

def DFS(v) :
    stack = list()
    component = list()

    stack.append(v)
    while stack :
        p = stack.pop()
        if p not in visited :
            visited.append(p)
            component.append(p)
        for n in adjacent_list[p] :
            if n not in visited :
                stack.append(n)
    connected_component.append(component)

def BFS(v) :
    queue = deque()
    component = list()

    queue.append(v)
    visited.append(v)
    component.append(v)
    while queue :
        p = queue.popleft()
        for n in adjacent_list[p] :
            if n not in visited :
                queue.append(n)
                visited.append(n)
                component.append(n)
    connected_component.append(component)

for v in range(1, len(adjacent_list)) :
    if v not in visited :
        DFS(v)
        # BFS(v)

print(len(connected_component))
print(connected_component)
print(visited)
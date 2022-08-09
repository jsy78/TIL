from collections import deque
V = int(input())
E = int(input())
adjacent_list = [[] for _ in range(V+1)]
visited = []
for _ in range(E) :
    v1, v2 = map(int, input().split())
    adjacent_list[v1].append(v2)
    adjacent_list[v2].append(v1)

def DFS(v) :
    visited.append(v)
    for i in range(len(adjacent_list[v])) :
        if adjacent_list[v][i] not in visited :
            DFS(adjacent_list[v][i])
    return

def BFS(v) :
    queue = deque()
    queue.append(v)
    visited.append(v)
    while queue :
        p = queue.popleft()
        for i in range(len(adjacent_list[p])) :
            if adjacent_list[p][i] not in visited :
                queue.append(adjacent_list[p][i])
                visited.append(adjacent_list[p][i])

BFS(1)
print(visited)
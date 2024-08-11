import sys
# sys.setrecursionlimit(10000)
input = sys.stdin.readline

V, E = map(int, input().split())
adjacent_list = [[] for _ in range(V+1)]
visited = []
component = []
connected_component = []

for _ in range(E) :
    v1, v2 = map(int, input().split())
    adjacent_list[v1].append(v2)
    adjacent_list[v2].append(v1)

def DFS(v) :
    visited.append(v)
    component.append(v)
    for i in range(len(adjacent_list[v])) :
        if adjacent_list[v][i] not in visited :
            DFS(adjacent_list[v][i])
    return
    

for v in range(1, len(adjacent_list)) :
    if v not in visited :
        DFS(v)
        connected_component.append(component.copy())
        component.clear()

print(connected_component)
print(visited)
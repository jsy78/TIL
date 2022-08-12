import sys

sys.stdin = open("_창용마을무리의개수.txt")

def DFS(i, graph_list, visited_list, component_list) :
    stack = list()
    component = list() # 요소 생성을 위한 리스트

    stack.append(i)
    while stack : # 스택이 빌 때까지
        p = stack.pop()
        if not visited_list[p] :
            visited_list[p] = True # 방문 안했으면 방문 처리
            component.append(p) # 인접한 정점 추가
        for n in graph_list[p] :
            if not visited_list[n] :
                stack.append(n) # 인접해있고 방문 안한 모든 정점 추가
    component_list.append(component) # 최종적으로 만들어진 요소 추가

T = int(input())
for test_case in range(1, T+1) :
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    connected_component = []

    for _ in range(E) :
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    for v in range(1, V+1) :
        if not visited[v] :
            DFS(v, graph, visited, connected_component)
    
    print(f'#{test_case} {len(connected_component)}')
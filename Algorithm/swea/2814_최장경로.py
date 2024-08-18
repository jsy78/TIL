def DFS(v, depth) :
    global result

    result = max(depth, result)
    
    for n in adjacent_list[v] :
        if not visited[n] :
            visited[n] = True
            DFS(n, depth+1)
            visited[n] = False

T = int(input())
for test_case in range(1, T+1) :
    V, E = map(int, input().split())
    
    adjacent_list = [[] for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    result = 0

    for _ in range(E) :
        v1, v2 = map(int, input().split())
        adjacent_list[v1].append(v2)
        adjacent_list[v2].append(v1)
    
    for v in range(1, V+1) :
        visited[v] = True
        DFS(v, 1)
        visited[v] = False

    print(f'#{test_case} {result}')
    
T = int(input())
for test_case in range(1, T+1) :
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M) :
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    result = 0
    for i in range(1, N+1) :
        for j in graph[i] :
            for k in graph[j] :
                if i < j < k and i in graph[k] :
                    result += 1
    
    print(f'#{test_case} {result}')
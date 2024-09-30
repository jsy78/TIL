import sys
sys.stdin = open('1219_길찾기.txt', 'r')

def DFS_iterative(v) :
    stack = list()

    stack.append(v)
    while stack :
        p = stack.pop()
        visited[p] = True
        for n in graph[p] :
            if not visited[n] :
                stack.append(n)

def DFS(v) :
    visited[v] = True
    for n in graph[v] :
        if not visited[n] :
            DFS(n)
    return


for test_case in range(1, 11) : 
    N, E = map(int, input().split())
    edge = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    visited = [False] * 100

    for i in range(0, E*2, 2) :
        graph[edge[i]].append(edge[i+1])

    DFS_iterative(0)

    if visited[99] :
        print(f'#{N} 1')
    else :
        print(f'#{N} 0')

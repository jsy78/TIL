import sys
from collections import deque
sys.stdin = open('1803_최단경로.txt', 'r')

def BFS(v) :
    queue = deque()
    queue.append(v)
    dist[v] = 0
    while queue :
        q = queue.popleft()
        for n, d in graph[q] :
            if dist[n] > dist[q] + d :
                dist[n] = dist[q] + d
                queue.append(n)

T = int(input())
for test_case in range(1, T+1) :
    N, M, start, end = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    dist = [float('inf') for _ in range(N+1)]
    for _ in range(M) :
        v1, v2, d = map(int, input().split())
        graph[v1].append((v2, d))
        graph[v2].append((v1, d))
    
    BFS(start)

    print(f'#{test_case} {dist[end]}')

sys.stdin.close()
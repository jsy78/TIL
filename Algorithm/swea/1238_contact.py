import sys
from collections import deque, defaultdict
sys.stdin = open('1238_contact.txt', 'r')

def BFS(v) :
    queue = deque()

    depth[v] += 1
    queue.append(v)
    while queue :
        q = queue.popleft()
        for n in graph[q] :
            if depth[n] == 0 :
                queue.append(n)
                depth[n] = max(depth[n], depth[q] + 1)

for test_case in range(1, 11) :
    N, start = map(int, input().split())
    edge = list(map(int, input().split()))
    graph = defaultdict(list)
    depth = [0] * 101

    for i in range(0, N, 2) :
        if edge[i+1] not in graph[edge[i]] :
            graph[edge[i]].append(edge[i+1])

    BFS(start)

    for i in range(100, 0, -1) :
        if depth[i] == max(depth) :
            print(f'#{test_case} {i}')
            break
    
sys.stdin.close()
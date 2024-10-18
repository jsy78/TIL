import sys, heapq
sys.stdin = open('1251_하나로.txt', 'r')

def tax(a, b) :
    return ((X[b]-X[a])**2 + (Y[b]-Y[a])**2) * E

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    # selected = [0]
    # tunnel = []
    # while len(selected) < N :
    #     min_dist = sys.maxsize
    #     min_edge = (0, 0)
    #     not_selected = [i for i in range(N) if i not in selected]
    #     for i in selected :
    #         for j in not_selected :
    #             if min_dist > tax(i, j) :
    #                 min_dist = tax(i, j)
    #                 min_edge = (i, j)
    #     tunnel.append(min_edge)
    #     selected.append(min_edge[1])
    
    # print(f'#{test_case} {sum(map(lambda x : tax(x[0], x[1]), tunnel)):.0f}')

    visited = [False] * N
    island = []
    weight_sum = 0
    heapq.heappush(island, (0, 0))
    while island :
        weight, v = heapq.heappop(island)
        
        if visited[v] :
            continue

        visited[v] = True
        weight_sum += weight

        for i in range(N) :
            if not visited[i] :
                heapq.heappush(island, (tax(v, i), i))
    
    print(f'#{test_case} {weight_sum:.0f}')
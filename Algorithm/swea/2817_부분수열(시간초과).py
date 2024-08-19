def sub_sum(lst, i, end, visited, k) :
    if sum(map(lambda x : x[1], visited)) == k and visited not in S:
        S.append(visited.copy())
        return
    
    if i == end :
        return
    
    if sum(map(lambda x : x[1], visited)) + lst[i] <= k and (i, lst[i]) not in visited:
        visited.add((i, lst[i]))
        sub_sum(lst, i+1, end, visited, k)
        visited.discard((i, lst[i]))
        sub_sum(lst, i+1, end, visited, k)

T = int(input())
for test_case in range(1, T+1) :
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = list()
    visited = set()

    sub_sum(A, 0, len(A), visited, K)
    print(f'#{test_case} {len(S)}')


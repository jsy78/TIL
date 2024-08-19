def sub_sum(lst, idx, end, visited) :
    if sum(visited) == K :
        S.append(visited.copy())
        return
    if idx == end :
        return
    visited.append(lst[idx])
    sub_sum(lst, idx+1, end, visited)
    visited.pop()
    sub_sum(lst, idx+1, end, visited)


T = int(input())
for test_case in range(1, T+1) :
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = list()
    visited = list()
    sub_sum(A, 0, len(A), visited)
    print(f'#{test_case} {len(S)}')


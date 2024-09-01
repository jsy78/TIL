T = int(input())
for test_case in range(1, T+1) :
    N, L = map(int, input().split())
    T = [0] * (N+1)
    K = [0] * (N+1)
    for i in range(1, N+1) :
        T[i], K[i] = map(int, input().split())

    DP = [0] * (L+1)
    for i in range(1, N+1) :
        for j in range(L, 0, -1) :
            if j - K[i] >= 0 :
                DP[j] = max(DP[j], DP[j-K[i]]+T[i])

    print(f'#{test_case} {DP[L]}')
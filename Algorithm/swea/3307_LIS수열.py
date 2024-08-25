T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    A = list(map(int, input().split()))
    DP = [1] * N

    for i in range(1, N) :
        for j in range(i) :
            if A[i] > A[j] :
                DP[i] = max(DP[i], DP[j]+1)

    print(f'#{test_case} {max(DP)}')

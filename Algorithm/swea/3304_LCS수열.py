T = int(input())
for test_case in range(1, T+1) :
    X, Y = input().split()
    m, n = len(X), len(Y)
    DP = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1) :
        for j in range(1, n+1) :
            if X[i-1] == Y[j-1] :
                DP[i][j] = DP[i-1][j-1]+1
            else :
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])

    print(f'#{test_case} {DP[m][n]}')

    # LCS 역추적
    # lcs = ''
    # i, j = m, n
    # while i > 0 and j > 0 :
    #     if DP[i][j] > DP[i][j-1] and DP[i][j] > DP[i-1][j-1] and DP[i][j] > DP[i-1][j] :
    #         i -= 1
    #         j -= 1
    #         lcs = X[i] + lcs
    #     elif DP[i][j] == DP[i][j-1] and DP[i][j] > DP[i-1][j] :
    #         j -= 1
    #     else :
    #         i -= 1
    # print(lcs)
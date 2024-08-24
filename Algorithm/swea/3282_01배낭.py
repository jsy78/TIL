# 시간초과
# def knapsack(i, k) :
#     if i == 0 or k <= 0 :
#         return 0
    
#     if V[i] <= k :
#         return max(knapsack(i-1, k), knapsack(i-1, k-V[i])+C[i])
#     else :
#         return knapsack(i-1, k)
    

# 2차원 DP
# T = int(input())
# for test_case in range(1, T+1) :
#     N, K = map(int, input().split()) # N개의 물건, 최대 부피 K
#     V = [0] * (N+1) # 부피
#     C = [0] * (N+1) # 가치
#     DP = [[0 for _ in range(K+1)] for _ in range(N+1)]
#     for i in range(1, N+1) :
#         V[i], C[i] = map(int, input().split())

#     for i in range(1, N+1) :
#         for j in range(1, K+1) :
#             if j - V[i] >= 0 :
#                 DP[i][j] = max(DP[i-1][j], DP[i-1][j-V[i]]+C[i])
#             else :
#                 DP[i][j] = DP[i-1][j]


#     print(f'#{test_case} {DP[N][K]}')

# 1차원 DP
T = int(input())
for test_case in range(1, T+1) :
    N, K = map(int, input().split()) # N개의 물건, 최대 부피 K
    V = [0] * (N+1) # 부피
    C = [0] * (N+1) # 가치
    DP = [0] * (K+1)
    for i in range(1, N+1) :
        V[i], C[i] = map(int, input().split())

    for i in range(1, N+1) :
        for j in range(K, 0, -1) :
            if j - V[i] >= 0 :
                DP[j] = max(DP[j], DP[j-V[i]]+C[i])

    print(f'#{test_case} {DP[K]}')
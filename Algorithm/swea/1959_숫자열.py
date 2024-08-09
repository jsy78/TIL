T = int(input())
for test_case in range(1, T+1) :
    N, M = map(int, input().split())
    A_lst = list(map(int, input().split()))
    B_lst = list(map(int, input().split()))
    
    sum_lst = []
    if N < M :
        for i in range(M-N+1) :
            result = 0
            C_lst = B_lst[i:i+N] 
            for j in range(N) :
                result += A_lst[j]*C_lst[j]
            sum_lst.append(result)
    elif N > M :
        for i in range(N-M+1) :
            result = 0
            C_lst = A_lst[i:i+M] 
            for j in range(M) :
                result += B_lst[j]*C_lst[j]
            sum_lst.append(result)
    else :
        result = 0
        for i in range(N) :
            result += A_lst[j]*B_lst[j]
        sum_lst.append(result)

    print(f'#{test_case} {max(sum_lst)}')
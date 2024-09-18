def check(num) :
    str_num = str(num)
    for i in range(len(str_num)-1) :
        if str_num[i] > str_num[i+1] :
            return False
    return True


T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    A = list(map(int, input().split()))

    max_num = -1
    for i in range(N-1) :
        for j in range(i+1, N) :
            num = A[i]*A[j]
            if check(num) :
                max_num = max(max_num, num)
    
    print(f'#{test_case} {max_num}')
T = int(input())
for test_case in range(1, T+1) :
    N, A, B = map(int, input().split())

    min_val = 9999999999
    for R in range(1, N+1):
        C = 1
        while R*C <= N :
            min_val =  min(min_val, A*abs(R-C) + B*(N-R*C))
            C += 1
    print(f'#{test_case} {min_val}')
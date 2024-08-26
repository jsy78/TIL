T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    print(f'#{test_case} {(N*(N+1))//2} {N*N} {N*(N+1)}')
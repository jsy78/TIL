T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    result = 0
    for _ in range(N) :
        P, X = map(float, input().split())
        result += P*X

    print(f'#{test_case} {result}')
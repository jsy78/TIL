T = int(input())
for test_case in range(1, T+1) :
    bus = [0] * 5001

    N = int(input())
    for _ in range(N) :
        A, B = map(int, input().split())
        for i in range(A, B+1) :
            bus[i] += 1

    result = []
    P = int(input())
    for _ in range(P) :
        C = int(input())
        result.append(bus[C])

    print(f'#{test_case}', *result)

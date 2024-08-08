T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    a = 0
    while N % 2 == 0 :
        N /= 2
        a += 1

    b = 0
    while N % 3 == 0 :
        N /= 3
        b += 1

    c = 0
    while N % 5 == 0 :
        N /= 5
        c += 1

    d = 0
    while N % 7 == 0 :
        N /= 7
        d += 1

    e = 0
    while N % 11 == 0 :
        N /= 11
        e += 1

    print(f'#{test_case} {a} {b} {c} {d} {e}')
T = int(input())
for test_case in range(1, T+1) :
    N = int(input())

    a = N // 50000
    b = N % 50000 // 10000
    c = N % 50000 % 10000 // 5000
    d = N % 50000 % 10000 % 5000 // 1000
    e = N % 50000 % 10000 % 5000 % 1000 // 500
    f = N % 50000 % 10000 % 5000 % 1000 % 500 // 100
    g = N % 50000 % 10000 % 5000 % 1000 % 500 % 100 // 50
    h = N % 50000 % 10000 % 5000 % 1000 % 500 % 100 % 50 // 10

    print(f'#{test_case}')
    print(f'{a} {b} {c} {d} {e} {f} {g} {h}')
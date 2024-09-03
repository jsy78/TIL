T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    
    print(f'#{test_case}', end=' ')
    for _ in range(N) :
        print(f'1/{N}', end=' ')
    print()
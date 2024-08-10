T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    num = list(map(int, input().split()))
    num.sort()
    print(f'#{test_case}', end=' ')
    print(*num, sep=' ', end='\n')
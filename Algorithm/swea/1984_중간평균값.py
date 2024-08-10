T = int(input())
for test_case in range(1, T+1) :
    num = list(map(int, input().split()))
    num.sort()
    print(f'#{test_case} {sum(num[1:9])/8:.0f}')
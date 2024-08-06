T = int(input())
for test_case in range(1, T+1) :
    num = list(map(int, input().split()))
    odd = [n for n in num if n%2 == 1]
    print(f'#{test_case} {sum(odd)}')
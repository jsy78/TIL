days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = [4, 5, 6, 0, 1, 2, 3]
T = int(input())
for test_case in range(1, T+1) :
    M1, D1 = 1, 1
    M2, D2 = map(int, input().split())
    total_day = sum(days[:M2])+D2 - (sum(days[:M1])+D1)
    print(f'#{test_case} {week[total_day%7]}')
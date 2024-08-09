T = int(input())
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for test_case in range(1, T+1) :
    M1, D1, M2, D2 = map(int, input().split())
    total_day1 = sum(days[:M1]) + D1
    total_day2 = sum(days[:M2]) + D2
    
    print(f'#{test_case} {total_day2 - total_day1 + 1}')
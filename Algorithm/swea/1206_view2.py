T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    building = list(map(int, input().split()))
    
    result = 0
    for i in range(2, N-2) :
        sub = building[i] - max(building[i-2], building[i-1], building[i+1], building[i+2])
        if sub > 0 :
            result += sub
    print(f'#{test_case} {result}')
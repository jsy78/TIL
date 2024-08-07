T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    prices = list(map(int, input().split()))
    benefit = 0

    max_val = prices[-1]
    for i in range(N-1, -1, -1) :
        if prices[i] >= max_val :
            max_val = prices[i]
        benefit += max_val-prices[i]
        
    print(f'#{test_case} {benefit}')



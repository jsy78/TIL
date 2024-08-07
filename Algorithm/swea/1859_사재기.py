T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    prices = list(map(int, input().split()))
    
    MAX_VALUE = [max(prices)]
    MAX_INDEX = [prices.index(MAX_VALUE[-1])]

    while MAX_INDEX[-1] < N-1 :
        MAX_VALUE.append(max(prices[MAX_INDEX[-1]+1:]))
        MAX_INDEX.append(prices.index(MAX_VALUE[-1], MAX_INDEX[-1]+1))

    benefit = 0
    start = 0
    for max_price, max_idx in zip(MAX_VALUE, MAX_INDEX) :
        benefit += max_price*(max_idx-start) - sum(prices[start:max_idx])
        start = max_idx+1
        
    print(f'#{test_case} {benefit}')



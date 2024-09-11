# https://velog.io/@changhee09/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%B9%B4%EB%8D%B0%EC%9D%B8-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
# https://medium.com/@vdongbin/kadanes-algorithm-%EC%B9%B4%EB%8D%B0%EC%9D%B8-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-acbc8c279f29

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    nums = list(map(int, input().split()))
    DP = [nums[0]] * N

    for i in range(1, N) :
        DP[i] = max(nums[i], nums[i]+DP[i-1])

    print(f'#{test_case} {max(DP)}')
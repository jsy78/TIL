T = int(input())
for test_case in range(1, T+1) :
    nums = list(map(int, input().split()))
    sum_set = set()
    for i in range(0, 5) :
        for j in range(i+1, 6) :
            for k in range(j+1, 7) :
                sum_set.add(nums[i]+nums[j]+nums[k])
    print(f'#{test_case} {sorted(list(sum_set), reverse=True)[4]}')
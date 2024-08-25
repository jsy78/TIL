from bisect import bisect_left # bisect_left([1,2,3,4],2) -> 1

def binary_search(lst, target) :
    left, right = 0, len(lst)-1
    while left <= right :
        mid = (left + right) // 2
        if lst[mid] < target :
            left = mid + 1
        else :
            right = mid - 1
    return left

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    A = list(map(int, input().split()))
    DP = []
    SUB = []
    LIS = []

    for a in A :
        i = bisect_left(DP, a)
        if len(DP) <= i :
            DP.append(a)
        else :
            DP[i] = a
        SUB.append((i, a))
    
    L_idx = len(DP)-1 
    for i in range(N-1, -1, -1) :
        if SUB[i][0] == L_idx :
            LIS.append(SUB[i][1])
            L_idx -= 1

    print(f'#{test_case} {len(DP)}')
    while LIS :
        print(LIS.pop(), end=' ')
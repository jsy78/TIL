# https://toastfactory.tistory.com/91
# https://hoho325.tistory.com/123

import sys, math
sys.stdin = open('1808_고장난계산기.txt', 'r')

def isPush(x : str) -> bool : 
    for c in x :
        if button[int(c)] == 0 :
            return False
    return True

def solve(x : int, count : int) -> int : 
    global min_val

    if isPush(str(x)) :
        if count == 0 :
            min_val = len(str(x)) + 1
        return len(str(x)) + 1
    
    result = -1
    for i in range(2, int(math.sqrt(x))+1, 1) :
        if x % i == 0 and isPush(str(i)) :
            a = len(str(i)) + 1
            b = solve(x//i, count+1)
            if b > -1 :
                result = a + b
                if result < min_val and x == X :
                    min_val = result
    return result

T = int(input())
for test_case in range(1, T+1) :
    button = list(map(int, input().split()))
    X = int(input())
    min_val = float('inf')

    solve(X, 0)

    if min_val == float('inf') :
        print(f'#{test_case} -1')
    else :
        print(f'#{test_case} {min_val}')
sys.stdin.close()
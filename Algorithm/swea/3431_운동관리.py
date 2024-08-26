def check(L, U, X) :
    if L <= X <= U :
        return 0
    elif L > X :
        return L-X
    elif X > U :
        return -1
 
T = int(input())
for test_case in range(1, T+1) :
    L, U, X = map(int, input().split())
    print(f'#{test_case} {check(L, U, X)}')
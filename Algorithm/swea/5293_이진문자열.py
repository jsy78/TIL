def solve(A, B, C, D) : 
    if A*D > 0 and B == 0 and C == 0:
        return 'impossible'
    
    if abs(B-C) > 1 :
        return 'impossible'
    
    if B == 0 and C == 0 :
        if A != 0 and D == 0 :
            return '0'*(A+1)
        elif A == 0 and D != 0 :
            return '1'*(D+1)
    else :
        if B < C :
           return '1'*D+'10'*C+'0'*A
        elif B > C :
            return '0'*A+'01'*B+'1'*D
        elif B == C :
            return '0'*A+'01'*B+'1'*D+'0'


T = int(input())
for test_case in range(1, T+1) :
    A, B, C, D = map(int, input().split()) # 00 01 10 11

    print(f'#{test_case} {solve(A, B, C, D)}')

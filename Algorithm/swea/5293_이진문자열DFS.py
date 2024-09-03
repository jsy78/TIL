def solve(S, A, B, C, D) : 
    global result
    
    if result != '' : # 이미 답을 찾은 경우
        return

    if abs(B-C) > 1 :
        return
    
    if A < 0 or B < 0 or C < 0 or D < 0 :
        return
    
    if A == 0 and B == 0 and C == 0 and D == 0 :
        result = S
        return
    
    if S[-1] == '0' :
        solve(S+'0', A-1, B, C, D)
        solve(S+'1', A, B-1, C, D)
    else :
        solve(S+'0', A, B, C-1, D)
        solve(S+'1', A, B, C, D-1)

T = int(input())
for test_case in range(1, T+1) :
    A, B, C, D = map(int, input().split()) # 00 01 10 11
    result = ''

    solve('0', A, B, C, D)
    solve('1', A, B, C, D)

    if result == '' :
        result = 'impossible'
    
    print(f'#{test_case} {result}')

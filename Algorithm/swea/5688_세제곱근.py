T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    
    i = 1
    while i**3 < N :
        i += 1
    
    if i**3 == N :
        print(f'#{test_case} {i}')
    else :
        print(f'#{test_case} -1')
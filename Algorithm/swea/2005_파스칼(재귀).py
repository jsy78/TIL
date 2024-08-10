def pascal(n : int) -> list :
    if n == 1 :
        return [1]
    else :
        return [1] + [pascal(n-1)[i]+pascal(n-1)[i+1] for i in range(len(pascal(n-1))-1)] + [1]

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    
    print(f'#{test_case}')
    for n in range(1, N+1) :
        print(*pascal(n), sep=' ')
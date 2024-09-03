T = int(input())
for test_case in range(1, T+1) :
    num = list(map(int, input()))
    
    print(f'#{test_case}', end=' ')
    if num[-1] % 2 == 0 :
        print('Even')
    else :
        print('Odd')
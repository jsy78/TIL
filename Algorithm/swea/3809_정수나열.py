T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    num = ''
    while len(num) != N :
        num = num + ''.join(input().split())
    
    i = 0
    while str(i) in num :
        i += 1
    
    print(f'#{test_case} {i}')
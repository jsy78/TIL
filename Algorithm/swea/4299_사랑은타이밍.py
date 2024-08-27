D1, H1, M1 = 11, 11, 11
T = int(input())
for test_case in range(1, T+1) :
    D2, H2, M2 = map(int, input().split())

    result = (D2-D1)*24*60 + (H2-H1)*60 + (M2-M1)

    if result < 0 :
        result = -1
    
    print(f'#{test_case} {result}')
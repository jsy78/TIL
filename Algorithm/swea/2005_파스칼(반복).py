T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    tri = [[0 for _ in range(N)] for _ in range(N)]
    
    tri[0][0] = 1
    for i in range(1, N) :
        for j in range(0, N) : 
            tri[i][j] = tri[i-1][j-1] + tri[i-1][j]

    print(f'#{test_case}')
    for i in range(N) :
        for j in range(N) : 
            if tri[i][j] != 0 :
                print(tri[i][j], end=' ') 
        print()
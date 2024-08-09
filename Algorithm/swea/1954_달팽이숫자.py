delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    
    r, c, d, n = 0, 0, 0, 2
    matrix[r][c] = 1
    while n != N*N+1 :
        nd = d % 4
        nr, nc = r + delta[nd][0], c + delta[nd][1]
        if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] == 0 :
            r, c = nr, nc
            matrix[r][c] = n
            n += 1
        else :
            d += 1
    print(f'#{test_case}')
    for i in range(N) :
        for j in range(N) :
            print(matrix[i][j], end=' ')
        print()
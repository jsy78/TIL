T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    matrix_90  = [[matrix[N-1-j][i] for j in range(N)] for i in range(N)]
    matrix_180 = [[matrix[N-1-i][N-1-j] for j in range(N)] for i in range(N)]
    matrix_270 = [[matrix[j][N-1-i] for j in range(N)] for i in range(N)]
    
    print(f'#{test_case}')
    for i in range(N) :
        print(*matrix_90[i], sep='', end=' ')
        print(*matrix_180[i], sep='', end=' ')
        print(*matrix_270[i], sep='', end=' ')
        print()
        
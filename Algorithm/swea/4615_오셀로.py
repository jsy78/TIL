delta = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))

T = int(input())
for test_case in range(1, T+1) :
    N, M = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    board[N//2-1][N//2] = board[N//2][N//2-1] = 1
    board[N//2-1][N//2-1] = board[N//2][N//2] = 2
    
    for _ in range(M) :
        x, y, c = map(int, input().split())
        x, y = x-1, y-1
        board[y][x] = c
        reverse = []
        for dy, dx in delta :
            ny, nx = y+dy, x+dx
            while True :
                if ny < 0 or nx < 0 or ny > N-1 or nx > N-1 :
                    reverse = []
                    break
                if board[ny][nx] == 0 :
                    reverse = []
                    break
                if board[ny][nx] == c :
                    break
                else :
                    reverse.append((ny, nx))
                ny, nx = ny+dy, nx+dx
            for ty, tx in reverse :
                board[ty][tx] = c
    print(f'#{test_case} {sum(map(lambda x : x.count(1), board))} {sum(map(lambda x : x.count(2), board))}')
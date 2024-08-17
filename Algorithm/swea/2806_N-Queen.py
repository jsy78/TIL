def isSafe(board, r, c) :
    N = len(board)

    for i in range(r-1, -1, -1) :
        if board[i][c] == 'Q' :
            return False
    for i, j in zip(range(r-1, -1, -1), range(c-1, -1, -1)) :
        if board[i][j] == 'Q' :
            return False
    for i, j in zip(range(r-1, -1, -1), range(c+1, N)) :
        if board[i][j] == 'Q' :
            return False
        
    return True

def solveNQueen(board, r) :
    N = len(board)
    global result

    if r == N :
        result += 1
        return

    for c in range(N) :
        if isSafe(board, r, c) :
            board[r][c] = 'Q'
            solveNQueen(board, r+1)
            board[r][c] = '.' 

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    board = [['.' for _ in range(N)] for _ in range(N)]
    result = 0
    solveNQueen(board, 0)
    print(f'#{test_case} {result}')
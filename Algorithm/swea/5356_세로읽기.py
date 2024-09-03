T = int(input())
for test_case in range(1, T+1) :
    board = [list(input()) for _ in range(5)]
    max_len = max(map(len, board))

    print(f'#{test_case}', end=' ')
    for i in range(max_len) :
        for j in range(5) :
            if i < len(board[j]) :
                print(board[j][i], end='')
    print()
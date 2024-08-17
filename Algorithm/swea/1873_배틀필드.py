T = int(input())
for test_case in range(1, T+1) :
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)]
    N = int(input())
    command = list(input())
    for cmd in command :
        if cmd == 'U' :
            for i in range(H) :
                for j in range(W) :
                    if board[i][j] in '^v<>' :
                        board[i][j] = '^'
                        if 0 <= i-1 < H and board[i-1][j] == '.' :
                            board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
                        break
        elif cmd == 'D' :
            for i in range(H-1, -1, -1) : # 행을 거꾸로 순회
                for j in range(W) :
                    if board[i][j] in '^v<>' :
                        board[i][j] = 'v'
                        if 0 <= i+1 < H and board[i+1][j] == '.' :
                            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                            break
                            
        elif cmd == 'L' :
            for i in range(H) :
                for j in range(W) :
                    if board[i][j] in '^v<>' :
                        board[i][j] = '<'
                        if 0 <= j-1 < W and board[i][j-1] == '.' :
                            board[i][j], board[i][j-1] = board[i][j-1], board[i][j]
                            break
                            
        elif cmd == 'R' :
            for i in range(H) :
                for j in range(W-1, -1, -1) : # 열을 거꾸로 순회
                    if board[i][j] in '^v<>' :
                        board[i][j] = '>'
                        if 0 <= j+1 < W and board[i][j+1] == '.' :
                            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                            break
                            
        elif cmd == 'S' :
            for i in range(H) :
                for j in range(W) :
                    if board[i][j] == '^' :
                        for k in range(i-1, -1, -1) :
                            if board[k][j] == '.' or board[k][j] == '-' :
                                continue
                            elif board[k][j] == '*' :
                                board[k][j] = '.'
                                break
                            elif board[k][j] == '#' :
                                break
                    elif board[i][j] == 'v' :
                        for k in range(i+1, H) :
                            if board[k][j] == '.' or board[k][j] == '-' :
                                continue
                            elif board[k][j] == '*' :
                                board[k][j] = '.'
                                break
                            elif board[k][j] == '#' :
                                break
                    elif board[i][j] == '<' :
                        for k in range(j-1, -1, -1) :
                            if board[i][k] == '.' or board[i][k] == '-' :
                                continue
                            elif board[i][k] == '*' :
                                board[i][k] = '.'
                                break
                            elif board[i][k] == '#' :
                                break
                    elif board[i][j] == '>' :
                        for k in range(j+1, W) :
                            if board[i][k] == '.' or board[i][k] == '-' :
                                continue
                            elif board[i][k] == '*' :
                                board[i][k] = '.'
                                break
                            elif board[i][k] == '#' :
                                break


    print(f'#{test_case}', end=' ')
    for i in range(H) :
        print(*board[i], sep='')
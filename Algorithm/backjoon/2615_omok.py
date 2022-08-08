import sys

sys.stdin = open('2615_omok.txt', 'r')

board = [list(map(int, input().split())) for _ in range(19)]
dr = [-1, 0, 1, 1]
dc = [ 1, 1, 1, 0]

for i in range(19) :
    for j in range(19) :
        if board[i][j] != 0 :
            for m in range(4) :
                cnt = 1
                nr = i + dr[m]
                nc = j + dc[m]

                while 0 <= nr < 19 and 0 <= nc < 19 and board[nr][nc] == board[i][j] :
                    cnt += 1
                    
                    if cnt == 5:
                        if 0 <= i-dr[m] < 19 and 0 <= j-dc[m] < 19 and board[i-dr[m]][j-dc[m]] == board[i][j] :
                            break
                        if 0 <= nr+dr[m] < 19 and 0 <= nc+dc[m] < 19 and board[nr+dr[m]][nc+dc[m]] == board[i][j] :
                            break

                        print(board[i][j])
                        print(i+1, j+1)
                        sys.exit(0)
                    
                    nr += dr[m]
                    nc += dc[m]
print(0)

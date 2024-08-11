delta = ((1, 0), (-1, 0)) # 1 : N극 (아래로), 2 : S극 (위로)
for test_case in range(1, 11) :
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N) :
        for j in range(N) :
            if table[i][j] == 1 :  
                r, c = i, j
                while True :
                    nr, nc = r + delta[0][0], c + delta[0][1]
                    if 0 <= nr < N and (table[nr][nc] == 0 or table[nr][nc] == 1):
                        table[r][c], table[nr][nc] = table[nr][nc], table[r][c]
                        r, c = nr, nc
                    elif 0 <= nr < N  and table[nr][nc] == 2 :
                        break
                    elif nr >= N :
                        table[r][c] = 0
                        break

            elif table[i][j] == 2 :
                r, c = i, j
                while True :
                    nr, nc = r + delta[1][0], c + delta[1][1]
                    if 0 <= nr < N and (table[nr][nc] == 0 or table[nr][nc] == 2):
                        table[r][c], table[nr][nc] = table[nr][nc], table[r][c]
                        r, c = nr, nc
                    if 0 <= nr < N and table[nr][nc] == 1 :
                        break
                    if nr < 0 :
                        table[r][c] = 0
                        break

    result = 0
    for i in range(N-1) :
        for j in range(N) :
            if table[i][j] == 1 and table[i+1][j] == 2 :
                result += 1

    print(f'#{test_case} {result}')
          

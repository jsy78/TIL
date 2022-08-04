from pprint import pprint

n = int(input())
mine_matrix = [list(input()) for _ in range(n)]
open_matrix = [list(input()) for _ in range(n)]

# 경계 채우기
mine_matrix.insert(0, ['.' for _ in range(n)])
open_matrix.insert(0, ['.' for _ in range(n)])
mine_matrix.insert(n+1, ['.' for _ in range(n)])
open_matrix.insert(n+1, ['.' for _ in range(n)])
for i in range(n+2) :
    mine_matrix[i].insert(0, '.')
    open_matrix[i].insert(0, '.')
    mine_matrix[i].insert(n+1, '.')
    open_matrix[i].insert(n+1, '.')

mine_list = []
for i in range(1, n+1) :
    for j in range(1, n+1) :
        if mine_matrix[i][j] == '.' :
            eight_list = [
                         mine_matrix[i-1][j-1], mine_matrix[i-1][j], mine_matrix[i-1][j+1],
                         mine_matrix[i][j-1],                        mine_matrix[i][j+1],
                         mine_matrix[i+1][j-1], mine_matrix[i+1][j], mine_matrix[i+1][j+1]
                         ]
            mine_count = eight_list.count('*')
            mine_matrix[i][j] = str(mine_count)
        elif mine_matrix[i][j] == '*' :
            mine_list.append((i, j))

mine_flag = False
for i in range(1, n+1) :
    for j in range(1, n+1) :
        if open_matrix[i][j] == 'x' and mine_matrix[i][j] == '*':
            mine_flag = True

if mine_flag == False :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            if open_matrix[i][j] == 'x' :
                open_matrix[i][j] = mine_matrix[i][j]

else :
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            if open_matrix[i][j] == 'x' :
                open_matrix[i][j] = mine_matrix[i][j]
    for (i, j) in mine_list :
        open_matrix[i][j] = '*'

for i in range(1, n+1) :
    for j in range(1, n+1) :
        print(open_matrix[i][j], end='')
    print()

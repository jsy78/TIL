from pprint import pprint
from sys import stdin

stdin = open('1063_king.txt', 'r')
input = stdin.readline

delta = {
     'R' : ( 0,  1),
     'L' : ( 0, -1),
     'B' : ( 1,  0),
     'T' : (-1,  0),
    'RT' : (-1,  1),
    'LT' : (-1, -1),
    'RB' : ( 1,  1),
    'LB' : ( 1, -1)
}
row = {
    '8' : 0,
    '7' : 1, 
    '6' : 2,
    '5' : 3,
    '4' : 4,
    '3' : 5,
    '2' : 6,
    '1' : 7
}
col = {
    'A' : 0,
    'B' : 1, 
    'C' : 2,
    'D' : 3,
    'E' : 4,
    'F' : 5,
    'G' : 6,
    'H' : 7
}
board = [['.' for _ in range(8)] for _ in range(8)]

king_pos, stone_pos, cnt = input().split()
cnt = int(cnt)

king_pos_r = row[king_pos[1]]
king_pos_c = col[king_pos[0]]
board[king_pos_r][king_pos_c] = 'K'

stone_pos_r = row[stone_pos[1]]
stone_pos_c = col[stone_pos[0]]
board[stone_pos_r][stone_pos_c] = 'S'

pprint(board)
for _ in range(cnt) :
    direction = input().strip('\n')
    king_pos_nr, king_pos_nc = king_pos_r + delta[direction][0], king_pos_c + delta[direction][1]
    if not (0 <= king_pos_nr < 8 and 0 <= king_pos_nc < 8) :
        continue

    if board[king_pos_nr][king_pos_nc] == 'S' :
        stone_pos_nr, stone_pos_nc = stone_pos_r + delta[direction][0], stone_pos_c + delta[direction][1]
        if not (0 <= stone_pos_nr < 8 and 0 <= stone_pos_nc < 8) :
            continue
        board[stone_pos_r][stone_pos_c], board[stone_pos_nr][stone_pos_nc] = board[stone_pos_nr][stone_pos_nc], board[stone_pos_r][stone_pos_c]
        stone_pos_r, stone_pos_c = stone_pos_nr, stone_pos_nc
    
    board[king_pos_r][king_pos_c], board[king_pos_nr][king_pos_nc] = board[king_pos_nr][king_pos_nc], board[king_pos_r][king_pos_c]
    king_pos_r, king_pos_c = king_pos_nr, king_pos_nc

    pprint(board)

king_pos = ''
stone_pos = ''
for k, v in col.items() :
    if v == king_pos_c :
        king_pos += k
    if v == stone_pos_c :
        stone_pos += k

for k, v in row.items() :
    if v == king_pos_r :
        king_pos += k
    if v == stone_pos_r :
        stone_pos += k

print(king_pos)
print(stone_pos)
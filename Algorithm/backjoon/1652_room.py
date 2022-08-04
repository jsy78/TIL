N = int(input())
rooms = [input() for _ in range(N)]
rooms_T = []
for i in range(N) :
    rooms_T.append([rooms[j][i] for j in range(N)])

for i in range(len(rooms_T)) :
    rooms_T[i] = ''.join(rooms_T[i])

row_count = 0
col_count = 0 

for bed in rooms : # 행 순회
    x_split = bed.split('X')
    for x in x_split :
        if len(x) >= 2 :
            row_count += 1

for bed in rooms_T : # 열 순회
    x_split = bed.split('X')
    for x in x_split :
        if len(x) >= 2 :
            col_count += 1

print(row_count, col_count)

chess = []
for _ in range(8) :
    chess.append(list(input()))

white = 0
for i in range(8) :
    for j in range(8) :
        if (i+j) % 2 == 0 and chess[i][j] == 'F':
            white += 1

print(white)
N, M = map(int, input().split())
castle = []

for _ in range(N) :
    castle.append(list(input()))

n, m = 0, 0
for i in range(N) :
    if 'X' not in castle[i] :
        n += 1

for j in range(M) :
    if 'X' not in [castle[i][j] for i in range(N)] :
        m += 1

print(max(n, m))
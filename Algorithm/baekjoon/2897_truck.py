R, C = map(int, input().split())
parking = [list(input()) for _ in range(R)]
delta = ((0, 0), (1, 0), (0, 1), (1, 1))
truck = []
crush = [0, 0, 0, 0, 0]

for r in range(R-1) :
    for c in range(C-1) :
        for dr, dc in delta :
            truck.append(parking[r+dr][c+dc])
        if truck.count('#') == 0 :
            crush[truck.count('X')] += 1
        truck.clear()

print(*crush, sep='\n')

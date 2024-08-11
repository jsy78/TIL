T = int(input())

for _ in range(T) :
    row, col = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(row)]

    zero_count = 0
    for c in range(col) : # 열 우선 순회
        for r in range(row) :
            if grid[r][c] == 1 :
                for i in range(r, row) : # 세로로 내려가며 0 세기
                    if grid[i][c] == 0 :
                        zero_count += 1
    print(zero_count)
def check(puzzle : list) -> int :
    number = set()
    for i in range(9) :
        for j in range(9) :
            number.add(puzzle[i][j])
        if len(number) != 9 :
            return 0
        number.clear()
    
    for i in range(9) :
        for j in range(9) :
            number.add(puzzle[j][i])
        if len(number) != 9 :
            return 0
        number.clear()

    for i in range(0, 9, 3) :
        for j in range(0, 9, 3) :
            for m in range(i, i+3) :
                for n in range(j, j+3) :
                    number.add(puzzle[m][n])
            if len(number) != 9 :
                return 0
            number.clear()
    
    return 1
    
T = int(input())
for test_case in range(1, T+1) :
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{test_case} {check(sudoku)}')
T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    building = list(map(int, input().split()))
    building_matrix = [[0]*255 for _ in range(N)]
    for i in range(N) :
        for j in range(building[i]) :
            building_matrix[i][j] = 1

    result = 0
    for i in range(N) :
        for j in range(building[i]) :
            if building_matrix[i][j] == 1 :
                if building_matrix[i-1][j] == 0 and building_matrix[i-2][j] == 0 and building_matrix[i+1][j] == 0 and building_matrix[i+2][j] == 0 :
                    result += 1

    print(f'#{test_case} {result}')
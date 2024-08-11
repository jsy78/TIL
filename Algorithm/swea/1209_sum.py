for _ in range(1, 11) :
    test_case = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    sum_lst = []

    for i in range(100) :
        result = 0
        for j in range(100) :
            result += matrix[i][j]
        sum_lst.append(result)
    
    for i in range(100) :
        result = 0
        for j in range(100) :
            result += matrix[j][i]
        sum_lst.append(result)

    result = 0
    for i in range(100) :
        for j in range(100) :
            if i == j :
                result += matrix[i][j]
        sum_lst.append(result)

    result = 0
    for i in range(100) :
        for j in range(100) :
            if i + j == 99 :
                result += matrix[i][j]
        sum_lst.append(result)
    
    print(f'#{test_case} {max(sum_lst)}')
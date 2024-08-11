for T in range(1, 11) :
    N = int(input())
    panel = [list(input()) for _ in range(8)]

    result = 0
    for i in range(8) :
        for j in range(8-N+1) :
            word = ''
            for k in range(j, j+N) :
                word += panel[i][k]
            if word == word[::-1] :
                result += 1
    
    for i in range(8-N+1) :
        for j in range(8) :
            word = ''
            for k in range(i, i+N) :
                word += panel[k][j]
            if word == word[::-1] :
                result += 1

    print(f'#{T} {result}')
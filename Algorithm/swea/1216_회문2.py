for _ in range(1, 11) :
    test_case = int(input())
    panel = [list(input()) for _ in range(100)]

    result = []
    for n in range(1, 101) :
        for i in range(100) :
            for j in range(100-n+1) :
                word = ''
                for k in range(j, j+n) :
                    word += panel[i][k]
                if word == word[::-1] :
                    result.append(word)
    
    for n in range(1, 101) :
        for i in range(100-n+1) :
            for j in range(100) :
                word = ''
                for k in range(i, i+n) :
                    word += panel[k][j]
                if word == word[::-1] :
                    result.append(word)

    print(f'#{test_case} {max(map(len, result))}')
for _ in range(1, 11) :
    test_case = int(input())
    panel = [list(input()) for _ in range(100)]
    panel_T = list(map(list, zip(*panel)))

    result = []
    for n in range(1, 101) :
        for i in range(100) :
            for j in range(100-n+1) :
                word = ''.join(panel[i][j:j+n])
                if word == word[::-1] :
                    result.append(word)
    
    for n in range(1, 101) :
        for i in range(100) :
            for j in range(100-n+1) :
                word = ''.join(panel_T[i][j:j+n])
                if word == word[::-1] :
                    result.append(word)

    print(f'#{test_case} {max(map(len, result))}')
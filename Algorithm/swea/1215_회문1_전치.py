for T in range(1, 11) :
    N = int(input())
    panel = [list(input()) for _ in range(8)]
    panel_T = list(map(list, zip(*panel)))

    result = 0
    for i in range(8) :
        for j in range(8-N+1) :
            word = ''.join(panel[i][j:j+N])
            if word == word[::-1] :
                result += 1
    
    for i in range(8) :
        for j in range(8-N+1) :
            word = ''.join(panel_T[i][j:j+N])
            if word == word[::-1] :
                result += 1

    print(f'#{T} {result}')
T = int(input())
for test_case in range(1, T+1) :
    S = input()
    
    diamond = [['.']*(4*len(S)+1) for _ in range(5)]
    for i in range(2, 4*len(S)+1, 4) :
        diamond[0][i] = '#'
        diamond[2][i] = S[(i-1)//4]
        diamond[4][i] = '#'
    for i in range(1, 4*len(S)+1, 2) :
        diamond[1][i] = '#'
        diamond[3][i] = '#'
    for i in range(0, 4*len(S)+1, 4) :
        diamond[2][i] = '#'
        

    for i in range(5) :
        for s in diamond[i] :
            print(s, end='')
        print()
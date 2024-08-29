T = int(input())
for test_case in range(1, T+1) :
    S = input()
    exist = True
    for (i, j) in zip(S, S[::-1]) :
        if i == '*' or j == '*' :
            break
        elif i != '*' and j != '*' and i != j:
            exist = False
            break

    if exist == True :
        print(f'#{test_case} Exist')
    else :
        print(f'#{test_case} Not exist')
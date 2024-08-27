T = int(input())
for test_case in range(1, T+1) :
    card = {'S' : [], 'D' : [], 'H' : [], 'C' : []}
    info = input()
    flag = True
    for i in range(0, len(info), 3) :
        if info[i+1:i+3] in card[info[i]] :
            print(f'#{test_case} ERROR')
            flag = False
            break
        card[info[i]].append(info[i+1:i+3])

    if flag == True:
        print(f'#{test_case}', end=' ')
        for v in card.values() :
            print(13-len(v), end=' ')
        print()
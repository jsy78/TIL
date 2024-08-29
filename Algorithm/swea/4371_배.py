T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    day = []
    for _ in range(N) :
        day.append(int(input()))

    lst = []
    for i in range(1, N) :
        lst.append(day[i]-day[0])

    for i in range(len(lst)) :
        for j in range(i+1, len(lst)) :
            if lst[i] == 0 :
                continue
            elif lst[j] % lst[i] == 0 :
                lst[j] = 0
    
    print(f'#{test_case} {len(list(filter(lambda x : x != 0, lst)))}')
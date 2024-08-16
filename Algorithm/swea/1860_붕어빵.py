T = int(input())
for test_case in range(1, T+1) :
    N, M, K = map(int, input().split())
    guest = sorted(list(map(int, input().split())))
    bread = [0] * (guest[-1]+1)


    k = 0
    for i in range(1, len(bread)) :
        if i % M == 0 :
            k += K
        bread[i] = k
    
    status = True
    for i in range(N) :
        if bread[guest[i]] <= 0 :
            status = False
            break
        else :
            for j in range(guest[i], len(bread)) :
                bread[j] -= 1

    if status :
        print(f'#{test_case} Possible')
    else :
        print(f'#{test_case} Impossible')
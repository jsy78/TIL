T = int(input())
for i in range(1, T+1) :
    sum = 0
    test_case = int(input())
    for j in range(1, test_case+1) :
        if j % 2 == 0 :
            sum -= j
        else :
            sum += j
    print(f'#{i} {sum}')
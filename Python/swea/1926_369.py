N = int(input())

for i in range(1, N+1) :
    s = str(i)
    cnt = 0
    for c in s :
        if c in '369' :
            cnt += 1
    if cnt == 0 :
        print(s, end='')
    else :
        for j in range(cnt):
            print('-', end='')
    print(' ', end='')
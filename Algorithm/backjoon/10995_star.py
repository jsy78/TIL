T = int(input())

if T == 1 :
    print('*')

else :
    for i in range(1, T+1) :
        if i%2 == 1 :
            for j in range(1, T*2+1) :
                if j%2 == 1 :
                    print('*', end='')
                else :
                    print(' ', end='')
        else :
            for j in range(1, T*2+1) :
                if j%2 == 1 :
                    print(' ', end='')
                else :
                    print('*', end='')
        print()
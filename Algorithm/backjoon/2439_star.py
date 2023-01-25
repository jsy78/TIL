T = int(input())

for i in range(T-1, -1, -1) : 
    for j in range(0, i) :
        print(' ', end='')
    for k in range(i, T) :
        print('*', end='')
    print()
    
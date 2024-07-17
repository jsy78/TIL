T = int(input())

for i in range(1, T+1) :
    star = list()
    for j in range(i) :
        star.append('*')
    string = ''.join(star)
    print(f'{string:>{T}}')

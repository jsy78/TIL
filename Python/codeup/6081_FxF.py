n = input()

if n == 'A' :
    n = 10
elif n == 'B' :
    n = 11
elif n == 'C' :
    n = 12
elif n == 'D' :
    n = 13
elif n == 'E' :
    n = 14
elif n == 'F' :
    n = 15
else :
    n = int(n)

for i in range(1, 16) :
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
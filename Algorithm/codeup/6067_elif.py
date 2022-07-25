a = int(input())
if a < 0 and a % 2 == 0 :
    print('A')
elif a < 0 and a % 2 != 0 :
    print('B')
elif a > 0 and a % 2 == 0 :
    print('C')
else :
    print('D')
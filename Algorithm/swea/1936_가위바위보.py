A, B = map(int, input().split())

# 1 : 가위 2 : 바위 3 : 보
if A == 1 and B == 2 :
    print('B')
elif A == 2 and B == 3 :
    print('B')
elif A == 3 and B == 1 :
    print('B')

elif A == 1 and B == 3 :
    print('A')
elif A == 2 and B == 1 :
    print('A')
elif A == 3 and B == 2 :
    print('A')
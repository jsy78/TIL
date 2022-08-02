import sys

input = sys.stdin.readline

T = int(input())
for i in range(T) :
    r, e, c = map(int, input().split())
    if r < e-c :
        print('advertise')
    elif r == e-c :
        print('does not matter')
    elif r > e-c :
        print('do not advertise')
import sys
input = sys.stdin.readline

cup = [None, 1, 0, 0]

M = int(input())
for _ in range(M) :
    x, y = map(int, input().split())
    cup[x], cup[y] = cup[y], cup[x]

try :
    print(cup.index(1))
except IndexError :
    print(-1)
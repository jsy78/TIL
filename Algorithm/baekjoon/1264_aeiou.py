import sys
input = sys.stdin.readline

while True :
    T = input().rstrip().lower()
    if T == '#' :
        break
    print(T.count('a')+T.count('e')+T.count('i')+T.count('o')+T.count('u'))
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    string = input().strip()
    while '()' in string :
        string = string.replace('()', '')
    
    if len(string) == 0 :
        print('YES')
    else :
        print('NO')
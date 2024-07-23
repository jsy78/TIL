import sys
input = sys.stdin.readline

string = input().strip().split('-')

for s in string :
    print(s[0], end='')
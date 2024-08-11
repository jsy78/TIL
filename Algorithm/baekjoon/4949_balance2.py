import sys

sys.stdin = open('4949_balance.txt', 'r')
input = sys.stdin.readline

while True :
    string = input().rstrip()
    if string == '.' :
        break
    for c in string :
        if c not in '()[]' :
            string = string.replace(c, '')

    for _ in string :
        while '()' in string :
            string = string.replace('()', '')
        while '[]' in string :
            string = string.replace('[]', '')
    
    if len(string) == 0 :
        print('yes')
    else :
        print('no')

sys.stdin.close()
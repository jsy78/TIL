import sys

sys.stdin = open('4949_balance.txt', 'r')
input = sys.stdin.readline

def check(string : str) -> str :
    stack = []
    for c in string :
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                return 'no'
        elif c == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop()
            else :
                return 'no'
    else :
        if len(stack) == 0 :
            return 'yes'
        else :
            return 'no'

while True :
    string = input().rstrip()
    if string == '.' :
        break
    print(check(string))

sys.stdin.close()
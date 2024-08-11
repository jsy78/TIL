import sys
input = sys.stdin.readline

stack = list()
start = input().rstrip()

while True :
    string = input().rstrip()

    if string == '문제' :
        stack.append(string)
    elif string == '고무오리' :
        if len(stack) == 0 :
            stack.extend(['고무오리', '고무오리'])
        else :
            stack.pop()
    elif string == '고무오리 디버깅 끝' :
        break

if len(stack) == 0 :
    print('고무오리야 사랑해') 
else :
    print('힝구')
import sys
sys.stdin = open('1223_계산기2.txt', 'r')

def to_postfix(infix : str) -> list:
    op = {'+' : 1, '-' : 1, '*' : 2, '/' : 2}
    postfix = ''
    number = ''
    stack = []
    for exp in infix :
        if exp.isdecimal() or exp == '.' :
            number += exp
        else :
            if number != '' :
                number += ' '
                postfix += number
                number = ''
            if exp == '(' :
                stack.append(exp)
            elif exp == ')' :
                while stack[-1] != '(' :
                    postfix += (stack.pop() + ' ')
                stack.pop()
            elif exp in op :
                if stack and stack[-1] != '(' and (op[stack[-1]] >= op[exp]) :
                    postfix += (stack.pop() + ' ')
                stack.append(exp)
    else :
        if number != '' :
            number += ' '
            postfix += number
            number = ''
    while stack :
        postfix += (stack.pop() + ' ')

    return postfix.split()

def eval_postfix(postfix : list[str]):
    stack = []
    for exp in postfix :
        if exp.isdecimal() :
            stack.append(int(exp))
        elif '.' in exp :
            stack.append(float(exp))
        else :
            n2 = stack.pop()
            n1 = stack.pop()
            if exp == '+' :
                result = n1 + n2
            elif exp == '-' :
                result = n1 - n2
            elif exp == '*' :
                result = n1 * n2
            elif exp == '/' :
                result = n1 / n2
            stack.append(result)
    
    return stack[0]

for test_case in range(1, 11) :
    N = int(input())
    infix = input()
    
    print(f'#{test_case} {eval_postfix(to_postfix(infix))}')
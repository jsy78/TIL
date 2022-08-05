import sys

sys.stdin = open("_괄호짝짓기.txt")

# 함수 사용법 힌트 작성
def check(word: str) -> int :
    close = {
        ')' : '(',
        ']' : '[', 
        '}' : '{',
        '>' : '<'
    }
    stack = []
    for c in word :
        if c in close.values() : # 여는 괄호
            stack.append(c) # 여는 괄호 push
        elif c in close.keys() : # 닫는 괄호
            if len(stack) == 0 : 
                return 0 # 닫는 괄호가 더 많아서 스택이 비었음
            elif stack[len(stack)-1] != close[c] : 
                return 0 # 괄호 짝이 서로 안 맞음
            elif stack[len(stack)-1] == close[c] : 
                stack.pop() # 괄호 짝이 맞으니 닫는 괄호 pop
        else : # 엉뚱한 문자가 들어옴
            return 0
    if len(stack) == 0 : 
        return 1 # 모든 괄호를 닫음
    else :               
        return 0 # 못 닫은 괄호가 남음

for test_case in range(1, 11) :
    word_len = int(input())
    word = input()

    print(f'#{test_case} {check(word)}')

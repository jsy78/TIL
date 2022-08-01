def check(s: str) -> bool :
    stk = []
    for c in s :
        if c == '(' :
            stk.append(c)
        else :
            if len(stk) == 0 :
                return False
            else :
                stk.pop()
    if len(stk) == 0 :
        return True
    else :
        return False


T = int(input())
for i in range(T) :
    if check(input()) == True :
        print('YES')
    else :
        print('NO')
    
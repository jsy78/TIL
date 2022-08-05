import sys
from collections import deque

sys.stdin = open("_암호생성기.txt")

for _ in range(10) :
    test_case = int(input())
    password = deque(map(int, input().split())) 
    # pop(0)보다 효율적인 deque 활용

    minus = 0
    while True :
        minus += 1
        num = password.popleft() # 맨 왼쪽에서 추출
        num -= minus # 처음엔 1부터 시작해서 2, 3, 4씩 빼기
        if num <= 0 : # 뺀 숫자가 0 또는 음수가 되면
            num = 0
            password.append(num) # 맨 오른쪽에 0 삽입 후 종료
            break
        password.append(num) # 뺀 숫자가 아직 양수임
        if minus == 5 : # 뺄 숫자가 5가 되면 다시 0으로 초기화
            minus = 0
    
    print(f'#{test_case}', end=' ')
    for i in range(8) :
        print(password[i], end=' ')
    print()




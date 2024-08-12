from collections import deque

for _ in range(10) :
    test_case = int(input())
    number = deque(map(int, input().split()))
    minus = 0
    while True :
        n = number.popleft()
        n -= ((minus % 5) + 1)
        if n <= 0 :
            n = 0
            number.append(n)
            break
        number.append(n)
        minus += 1
    print(f'#{test_case}', end=' ')
    print(*number, sep=' ')
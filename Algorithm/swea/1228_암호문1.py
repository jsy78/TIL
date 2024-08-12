from collections import deque

for test_case in range(1, 11) :
    N = int(input())
    original = list(map(int, input().split()))
    cmd_num = int(input())
    cmd_list = deque(input().split('I'))

    cmd_list.popleft()

    for _ in range(cmd_num) :
        cmd = cmd_list.popleft()
        cmd_list.append(list(map(int, cmd.split())))
    
    for _ in range(cmd_num) :
        cmd = cmd_list.popleft()
        for i in range(cmd[1]+1, 1, -1) :
            original.insert(cmd[0], cmd[i])

    print(f'#{test_case}', end=' ')
    for i in range(10) :
        print(f'{original[i]} ', end='') # 10개만 출력
    print()
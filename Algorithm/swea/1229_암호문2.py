from collections import deque

for test_case in range(1, 11) :
    N = int(input())
    original = list(map(int, input().split()))
    cmd_num = int(input())
    cmd_input = deque(input().split())
    cmd_list = list()

    for _ in range(cmd_num) :
        cmd = cmd_input.popleft()
        if cmd == 'I' :
            tmp = [cmd]
            x = int(cmd_input.popleft())
            tmp.append(x)
            y = int(cmd_input.popleft())
            tmp.append(y)
            for _ in range(y) :
                s = int(cmd_input.popleft())
                tmp.append(s)
            cmd_list.append(tmp)
        elif cmd == 'D' :
            tmp = [cmd]
            x = int(cmd_input.popleft())
            tmp.append(x)
            y = int(cmd_input.popleft())
            tmp.append(y)
            cmd_list.append(tmp)
    
    for cmd in cmd_list :
        if cmd[0] == 'I' :
            for i in range(cmd[2]+2, 2, -1) :
                original.insert(cmd[1], cmd[i])
        elif cmd[0] == 'D' :
            for i in range(cmd[2]) :
                del original[cmd[1]]

    print(f'#{test_case}', end=' ')
    for i in range(10) :
        print(f'{original[i]} ', end='') # 10개만 출력
    print()
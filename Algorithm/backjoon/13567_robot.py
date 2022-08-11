from sys import stdin

stdin = open('13567_robot.txt', 'r')
input = stdin.readline

M, command_count = map(int, input().split())
area = [['.' for _ in range(M)] for _ in range(M)]
robot_r, robot_c = M-1, 0
area[robot_r][robot_c] = 'R'
vector = [0, 1]

for _ in range(command_count) :
    command, number = input().strip('\n').split()
    number = int(number)

    if command == 'MOVE' :
        nr = robot_r + (vector[0] * number)
        nc = robot_c + (vector[1] * number)
        if not (0 <= nr < M and 0 <= nc < M) :
            print(-1)
            break
        area[robot_r][robot_c], area[nr][nc] = area[nr][nc], area[robot_r][robot_c]
        robot_r, robot_c = nr, nc
    elif command == 'TURN' :
        if number == 0 :
            vector[0], vector[1] = (0 * vector[0]) + (-1 * vector[1]), ( 1 * vector[0]) + (0 * vector[1]) 
        elif number == 1 :
            vector[0], vector[1] = (0 * vector[0]) + ( 1 * vector[1]), (-1 * vector[0]) + (0 * vector[1])
        else :
            print(-1)
            break
    else :
        print(-1)
        break
else :
    robot_x = robot_c
    robot_y = (M-1) - robot_r
    print(robot_x, robot_y)



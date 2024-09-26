import sys
sys.stdin = open('1210_사다리.txt', 'r')

delta = ((-1, 0), (0, -1), (0, 1)) # 위쪽, 왼쪽, 오른쪽
for _ in range(10) :
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    destination = []
    direction = []
    path = []

    for i in range(100) :
        if ladder[99][i] == 1 :
            destination.append(i)

    for i in range(len(destination)) :
        r, c = 99, destination[i]
        while True :
            if r == 0 :
                break
            if 0 < c < 99 :
                if ladder[r][c-1] == ladder[r][c+1] == 0 :
                    direction.append(delta[0])
                elif ladder[r][c-1] == ladder[r][c+1] == 1 :
                    direction.append(direction[-1])
                elif ladder[r][c-1] != ladder[r][c+1] :
                    if direction[-1] == delta[0] :
                        if ladder[r][c-1] == 1 :
                            direction.append(delta[1])
                        elif ladder[r][c+1] == 1 :
                            direction.append(delta[2])
                    else :
                        direction.append(delta[0])
            elif c == 0 :
                if ladder[r][c+1] == 0 :
                    direction.append(delta[0])
                else :
                    if direction[-1] != delta[0] :
                        direction.append(delta[0])
                    else :
                        direction.append(delta[2])
            elif c == 99 :
                if ladder[r][c-1] == 0 :
                    direction.append(delta[0])
                else :
                    if direction[-1] != delta[0] :
                        direction.append(delta[0])
                    else :
                        direction.append(delta[1])

            r, c = r + direction[-1][0], c + direction[-1][1]
        path.append((c, len(direction)))
        direction.clear()
    
    path.sort(key=lambda x : x[1])
    print(f'#{N} {path[0][0]}')
sys.stdin.close()
import sys

sys.stdin = open("_파리퇴치.txt")

T = int(input())

for test_case in range(1, T+1) :
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    die = []
    '''
    1 x 1 = (i, j)
    2 x 2 = (i, j), (i, j+1), (i+1, j), (i+1, j+1)
    3 x 3 = (i, j), (i, j+1), (i, j+2), (i+1, j), (i+1, j+1), (i+1, j+2), (i+2, j), (i+2, j+1), (i+2, j+2)
    .
    .
    m x m = (i, j), ... , (i, j+m-1), ... , (i+m-1, j), ... , (i+m-1, j+m-1)
    '''
    for i in range(N) :
        if i+M-1 >= N : # 파리채 가로 크기가 공간을 넘으면 continue
            continue
        for j in range(N) :
            if j+M-1 >= N : # 파리채 세로 크기가 공간을 넘으면 continue
                continue
            tool = []
            for x in range(i, i+M): # 파리채 가로 길이 : i ~ i+M
                for y in range(j, j+M) : # 파리채 세로 길이 : j ~ j+M
                    tool.append(fly[x][y]) # 파리채로 죽인 파리들
            die.append(sum(tool)) # 파리채로 죽인 파리들의 합
    print(f'#{test_case} {max(die)}')




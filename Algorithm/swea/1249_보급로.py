import sys
from collections import deque
sys.stdin = open('1249_보급로.txt', 'r')

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

def BFS(r, c) :
    queue = deque()
    time[r][c] = road[r][c]
    queue.append((r, c))
    while queue :
        qr, qc = queue.popleft()
        for dr, dc in delta :
            nr, nc = qr + dr, qc + dc
            if 0 <= nr < N and 0 <= nc < N :
                if time[nr][nc] > time[qr][qc] + road[nr][nc] :
                    time[nr][nc] = time[qr][qc] + road[nr][nc]
                    queue.append((nr, nc))

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    road = [list(map(int, input())) for _ in range(N)]
    time = [[sys.maxsize for _ in range(N)] for _ in range(N)]

    BFS(0, 0)
    print(f'#{test_case} {time[N-1][N-1]}')
sys.stdin.close()
import sys

sys.stdin = open("_등산로조성.txt")

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

def DFS_construction(r, c, limit, length) : # 현재 위치 좌표, 공사 가능 횟수, 현재 길이
    global max_length

    if visited[r][c] == 1 : # 현재 위치 방문 여부 체크
        return

    visited[r][c] = 1 # 현재 위치 방문

    for dr, dc in delta :
        nr, nc = r + dr, c + dc # 다음 위치 좌표
        
        if not (0 <= nr < N and 0 <= nc < N) : # 범위 체크
            continue
        
        if visited[nr][nc] == 1 : # 다음 위치의 방문 여부 체크
            continue
        
        if mountain[nr][nc] < mountain[r][c] : # 다음 위치의 원래 높이가 기존 위치의 높이보다 낮음 
            DFS_construction(nr, nc, limit, length+1) # 다음 위치 좌표 및 높이, 공사 안 함, 길이 증가
        
        elif mountain[nr][nc] >= mountain[r][c] and limit > 0 : # 다음 위치의 원래 높이가 기존 위치보다 높거나 같고 공사 가능 횟수 남음
            for i in range(1, K+1) :
                mountain[nr][nc] -= i # 다음 위치의 높이를 정수 단위로 최대 K만큼 깎음
                if mountain[nr][nc] < mountain[r][c] : # 깎은 높이가 기존 높이보다 낮아지면
                    DFS_construction(nr, nc, limit-1, length+1) # 다음 위치 좌표 및 높이, 공사 가능 횟수 감소, 길이 증가   
                mountain[nr][nc] += i # 다음 위치의 높이 복구
    
    max_length = max(max_length, length) # 길이 갱신

    visited[r][c] = 0 # 끝자락에 도달했으면 역순으로 되돌아가면서 방문 해제

T = int(input())
for test_case in range(1, T+1) :
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    high_len = max(map(max, mountain))
    max_length = 0

    for i in range(N) :
        for j in range(N) :
            if mountain[i][j] == high_len :           
                DFS_construction(i, j, 1, 1)

    print(f'#{test_case} {max_length}')
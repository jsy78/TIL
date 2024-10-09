import sys
sys.stdin = open('1226_미로1.txt', 'r')

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
def DFS(r, c) :
    if visited[r][c] :
        return
    
    visited[r][c] = True

    for dr, dc in delta :
        nr, nc = r + dr, c + dc
        if 0 <= nr < 16 and 0 <= nc < 16 :
            if maze[nr][nc] == 0 or maze[nr][nc] == 3 and not visited[nr][nc] :
                DFS(nr, nc)
    return


for test_case in range(1, 11) : 
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[False for _ in range(16)] for _ in range(16)]

    for i in range(16) :
        for j in range(16) :
            if maze[i][j] == 2 :
                DFS(i, j)
    
    for i in range(16) :
        for j in range(16) :
            if maze[i][j] == 3 :
                if visited[i][j] :
                    print(f'#{N} 1')
                else :
                    print(f'#{N} 0')
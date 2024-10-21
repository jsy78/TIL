import sys
sys.stdin = open('1258_행렬찾기.txt', 'r')

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    sub_matrix = []

    for i in range(N) :
        for j in range(N) :
            if matrix[i][j] != 0 and visited[i][j] == 0 :
                r, c = 0, 0
                for n in range(i, N) :
                    for m in range(j, N) :
                        if matrix[n][m] == 0 :
                            break
                        visited[n][m] = 1
                        c += 1
                    if matrix[n][j] == 0 :
                        break
                    r += 1
                sub_matrix.append((r, c//r))
    
    sub_matrix.sort(key=lambda x : (x[0]*x[1], x[0]))
    print(f'#{test_case} {len(sub_matrix)}', end=' ')
    for row, col in sub_matrix :
        print(row, col, end=' ')
    print()
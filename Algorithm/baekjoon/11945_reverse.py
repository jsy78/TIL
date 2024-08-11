import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]

for i in range(N) :
    for j in range(M-1, -1, -1) :
        print(matrix[i][j], end='')
    print()
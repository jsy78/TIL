import sys

sys.stdin = open('7568_덩치.txt', 'r')
input = sys.stdin.readline

N = int(input())
body = [tuple(map(int, input().split())) for _ in range(N)]

rank = 1
for (x, y) in body :
    for (i, j) in body :
        if i > x and j > y :
            rank += 1
    print(rank, end=' ')
    rank = 1

sys.stdin.close()


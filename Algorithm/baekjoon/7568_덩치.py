import sys

sys.stdin = open('7568_덩치.txt', 'r')

T = int(input())

body = []
ranking = []
for i in range(1, T+1) :
    x, y = map(int, input().split())
    body.append((x, y))

rank = 1
for (i, j) in body :
    for (x, y) in body :
        if i < x and j < y :
            rank += 1
    ranking.append(rank)
    rank = 1

for r in ranking :
    print(r, end=" ")

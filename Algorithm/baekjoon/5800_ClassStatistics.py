from sys import stdin

input = stdin.readline

K = int(input())
for k in range(1, K+1) :
    score = list(map(int, input().split()))
    n = score.pop(0)

    score.sort(reverse=True)
    gap = 0

    for i in range(n-1) :
        if score[i] - score[i+1] > gap :
            gap = score[i] - score[i+1]

    print(f'Class {k}')
    print(f'Max {score[0]}, Min {score[-1]}, Largest gap {gap}')
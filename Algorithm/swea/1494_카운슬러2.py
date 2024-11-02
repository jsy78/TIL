# https://dream-programmer.tistory.com/m/6

import sys
from itertools import combinations

sys.stdin = open('1494_카운슬러.txt', 'r')

def vectorSize(x, y) :
    return x*x + y*y

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    point = [tuple(map(int, input().split())) for _ in range(N)]
    combi = list(combinations(range(N), N//2))
    min_vector = float('inf')

    for i in range(len(combi)) :
        x, y = 0, 0
        for j in range(N) :
            if j in combi[i] :
                x += point[j][0]
                y += point[j][1]
            else :
                x -= point[j][0]
                y -= point[j][1]
        min_vector = min(min_vector, vectorSize(x, y))

    print(f'#{test_case} {min_vector}')
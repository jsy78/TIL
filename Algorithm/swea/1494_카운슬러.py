# https://taegyunwoo.github.io/algorithm/ALGORITHM_Combination
# https://forswdev.tistory.com/m/entry/Sw-Expert-Academy-1494-사랑의-카운슬러-C

import sys
sys.stdin = open('1494_카운슬러.txt', 'r')

def vectorSize(x, y) :
    return x*x + y*y

def getCombination(idx, n, r) :
    global min_vector

    if r == 0 : # 뽑아야하는 만큼 뽑았으므로, 수행 후 종료
        x, y = 0, 0
        for i in range(n) :
            if visited[i] :
                x += point[i][0]
                y += point[i][1]
            else :
                x -= point[i][0]
                y -= point[i][1]
        min_vector = min(min_vector, vectorSize(x, y))
        return
    if idx == n : # 모든 원소를 둘러보았으므로, 종료
        return
    
    visited[idx] = True # 현재 원소를 뽑았을 때
    getCombination(idx+1, n, r-1) # n-1Cr-1

    visited[idx] = False # 현재 원소를 뽑지 않았을 때
    getCombination(idx+1, n, r) # n-1Cr


T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    point = [tuple(map(int, input().split())) for _ in range(N)]
    visited = [False for _ in range(N)]
    min_vector = float('inf')

    getCombination(0, N, N//2)

    print(f'#{test_case} {min_vector}')
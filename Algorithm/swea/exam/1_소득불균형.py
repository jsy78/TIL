import sys
from statistics import mean
# 예전 강의에서 표준편차 구하기 예시를 들었던 게 떠올라서 가져와봄
sys.stdin = open("_소득불균형.txt")

T = int(input())

for i in range(1, T+1) :
    n = int(input())
    person = list(map(int, input().split()))
    avg = mean(person)
    # 예상대로 평균 구하는 내장함수가 있었음
    cnt = 0
    for p in person :
        if p <= avg :
            cnt += 1
    
    print(f'#{i} {cnt}')
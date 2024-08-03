import sys
input = sys.stdin.readline

Q1 = Q2 = Q3 = Q4 = AXIS = 0
T = int(input())
for _ in range(T) :
    p1, p2 = map(int, input().split())
    if p1 * p2 == 0 :
        AXIS += 1
    else :
        if p1 > 0 and p2 > 0 :
            Q1 += 1
        elif p1 < 0 and p2 > 0 :
            Q2 += 1
        elif p1 < 0 and p2 < 0 :
            Q3 += 1
        elif p1 > 0 and p2 < 0 :
            Q4 += 1

print(f'Q1: {Q1}')
print(f'Q2: {Q2}')
print(f'Q3: {Q3}')
print(f'Q4: {Q4}')
print(f'AXIS: {AXIS}')
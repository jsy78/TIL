import sys
input = sys.stdin.readline

truck = [0] * 100
A, B, C = map(int, input().split())
for _ in range(3) :
    n, m = map(int, input().split())
    for i in range(n, m) :
        truck[i] += 1

fee = 0
for t in truck :
    if t == 1 :
        fee += A
    elif t == 2 :
        fee += B*2
    elif t == 3 :
        fee += C*3
print(fee)
    
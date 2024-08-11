import sys
input = sys.stdin.readline

seq = []
for i in range(1, 46) :
    for j in range(i) :
        seq.append(i)
    
a, b = map(int, input().split())
print(sum(seq[a-1:b]))
import sys
input = sys.stdin.readline

sum_ = 0
X = int(input())
N = int(input())
for _ in range(N) : 
    a, b = map(int, input().split())
    sum_ += (a * b)
print('Yes') if X == sum_ else print('No')
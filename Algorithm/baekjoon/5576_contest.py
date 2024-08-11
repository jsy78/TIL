import sys
input = sys.stdin.readline

W = [int(input()) for _ in range(10)]
K = [int(input()) for _ in range(10)]

print(sum(sorted(W, reverse=True)[0:3]))
print(sum(sorted(K, reverse=True)[0:3]))

# https://www.acmicpc.net/problem/8393

from sys import stdin

input = stdin.readline

N = int(input())

print(f'{int(N * (N+1) / 2)}')

# print(sum(range(1, N+1)))

# sum = 0
# for i in range(1, N+1) :
#     sum += i

# print(sum)
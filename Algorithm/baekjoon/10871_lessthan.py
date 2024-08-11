# https://www.acmicpc.net/problem/10871
from sys import stdin

input = stdin.readline

N, X = map(int, input().split())
number = list(map(int, input().split()))
for i in range(N) :
    if number[i] < X :
        print(number[i], end=' ')
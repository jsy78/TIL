# https://www.acmicpc.net/problem/1065

import sys

N = int(sys.stdin.readline())

count = 0
for i in range(1, N+1):
    if 1 <= i <= 99 :
        count += 1
    if 100 <= i <= 999 :
        c = i % 100 % 10  #   1의 자리
        b = i % 100 // 10 #  10의 자리
        a = i // 100      # 100의 자리
        if a - b == b - c :
            count += 1
print(count)
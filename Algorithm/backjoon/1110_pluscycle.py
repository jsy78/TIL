# https://www.acmicpc.net/problem/1110

import sys

N = int(sys.stdin.readline())

num = N
count = 0
while True :
    if num < 10 :
        a, b = 0, num
    else :
        a, b = num // 10, num % 10

    c = a + b

    if c < 10 :
        a, b = b, c
    else :
        a, b = b, c % 10

    num = a*10 + b
    count += 1

    if num == N :
        break
print(count)   

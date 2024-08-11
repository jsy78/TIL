from sys import stdin

input = stdin.readline

N = int(input())
number = dict()

for _ in range(N) :
    n = int(input())
    if n in number :
        number[n] += 1
    else :
        number[n] = 1

for n in sorted(number.keys()) :
    if number[n] == max(number.values()) :
        print(n)
        break
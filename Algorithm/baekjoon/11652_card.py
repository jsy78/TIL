from sys import stdin
from collections import Counter

input = stdin.readline

N = int(input())
number = list()
for n in range(N) :
    number.append(int(input()))

print(sorted(Counter(number).most_common(), key = lambda x : (-x[1], x[0]))[0][0])

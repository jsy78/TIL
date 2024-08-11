from collections import Counter
from statistics import mean
from sys import stdin

input = stdin.readline

number = [int(input()) for _ in range(10)]
print(mean(number))
print(Counter(number).most_common(1)[0][0])

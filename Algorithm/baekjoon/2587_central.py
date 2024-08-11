from collections import Counter
from statistics import mean, median
from sys import stdin

input = stdin.readline

number = [int(input()) for _ in range(5)]
print(mean(number))
print(median(number))
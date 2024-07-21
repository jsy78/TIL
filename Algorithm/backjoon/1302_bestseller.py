from collections import Counter
from sys import stdin

input = stdin.readline

N = int(input())
book = [input().strip() for _ in range(N)]

print(sorted(Counter(book).most_common(), key=lambda x : (-x[1], x[0]))[0][0])
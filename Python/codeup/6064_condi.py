a, b, c = map(int, input().split())
min = (a if a < b else b) if ((a if a < b else b) < c) else c
print(min)
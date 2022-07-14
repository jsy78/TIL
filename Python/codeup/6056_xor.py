a, b = map(int, input().split())
a, b = map(bool, (a, b))
print(((not a) and b) or (a and (not b)))
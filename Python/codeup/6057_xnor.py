a, b = map(bool, map(int, input().split()))
print((a or (not b)) and ((not a) or b))
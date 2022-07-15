a, m, d, n = map(int, input().split())

for i in range(n-1) :
    t = a
    t *= m
    t += d
    a = t

print(a)
import sys

input = sys.stdin.readline

N = int(input())

result = 0
for i in range(1, N+1) :
    a = i // 10**6 
    b = i % 10**6 // 10**5
    c = i % 10**6 % 10**5 // 10**4
    d = i % 10**6 % 10**5 % 10**4 // 10**3
    e = i % 10**6 % 10**5 % 10**4 % 10**3 // 10**2
    f = i % 10**6 % 10**5 % 10**4 % 10**3 % 10**2 // 10
    g = i % 10**6 % 10**5 % 10**4 % 10**3 % 10**2 % 10
    if i + a + b + c + d + e + f + g == N :
        result = i
        break

print(result)

n = int(input())
a = list(map(int, input().split()))

m = a[0]
for i in range(n) :
    if a[i] < m :
        m = a[i]
print(m)
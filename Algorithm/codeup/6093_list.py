n = int(input())
a = list(map(int, input().split()))

for i in range(n-1, -1, -1) :
    print(a[i], end=' ')
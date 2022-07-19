from math import log10

num = int(input())
case = int(log10(num))+1
sum = 0
for i in range(case-1, -1, -1):
    sum += (num // 10**i)
    num -= ((num // 10**i) * 10**i)
print(sum)

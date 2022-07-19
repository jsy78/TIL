from math import log10

num = int(input())
numlist = []
case = int(log10(num))+1
for i in range(case-1, -1, -1):
    numlist.append(num // 10**i)
    num -= ((num // 10**i) * 10**i)

for j in range(len(numlist)-1, -1, -1) :
    print(numlist[j], end='')
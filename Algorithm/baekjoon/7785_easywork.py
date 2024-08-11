import sys
input = sys.stdin.readline
company = dict()

N = int(input())
for _ in range(N) :
    name, word = input().split()
    company[name] = word

lst = list()
for name in company.keys() :
    if company[name] == 'enter' :
        lst.append(name)

for name in sorted(lst, reverse=True) :
    print(name)
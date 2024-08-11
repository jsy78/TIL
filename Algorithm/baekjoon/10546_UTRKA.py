import sys
input = sys.stdin.readline

N = int(input())
name = dict()
for _ in range(N) :
    key = input().rstrip()
    if key not in name :
        name[key] = 1
    else :
        name[key] += 1

for _ in range(N-1) :
    key = input().rstrip()
    name[key] -= 1

for key, value in name.items() :
    if value != 0 :
        print(key)
        break

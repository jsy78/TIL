import sys
input = sys.stdin.readline

seat = [False] * 101

N = int(input())
guest = tuple(map(int, input().split()))
rejected = 0

for n in guest :
    if seat[n] == False :
        seat[n] = True
    else :
        rejected += 1

print(rejected)

import sys
input = sys.stdin.readline

agents = [input().rstrip() for _ in range(5)]
FBI = [0] * 5

for i in range(5) :
    if agents[i].count('FBI') > 0 :
        FBI[i] = 1

if sum(FBI) == 0 :
    print('HE GOT AWAY!')
else :
    for i, f in enumerate(FBI) :
        if f != 0 :
            print(i+1, end=' ')
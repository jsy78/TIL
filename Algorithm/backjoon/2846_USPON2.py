import sys

input = sys.stdin.readline

N = int(input())
route = list(map(int, input().split()))
climb = list()
tmp = []

for i in range(N-1) :
    if route[i+1] - route[i] > 0 :
        if len(tmp) == 0 :
            tmp.append(route[i])
            tmp.append(route[i+1])
        else :
            tmp.append(route[i+1])
    else :
        if len(tmp) > 0 :
            climb.append(tmp[:])
            tmp.clear()
else :    
    if len(tmp) > 0 :
        climb.append(tmp[:])
        tmp.clear()

try :
    print(max(map(lambda lst : max(lst)-min(lst), climb)))        
except ValueError :
    print(0)
    

import sys 
input = sys.stdin.readline

N = int(input())
for n in range(N, -1, -1) :
    for x in '01235689' :
        if x in str(n) :
            break
    else :
        print(n)
        break
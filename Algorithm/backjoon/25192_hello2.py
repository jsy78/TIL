import sys

input = sys.stdin.readline

N = int(input())
chat = [input().rstrip() for _ in range(N)]
ENTER_index = list(filter(lambda x : chat[x] == 'ENTER', range(len(chat))))
hello = 0

for i in range(len(ENTER_index)-1) :
    hello += len(set(chat[ENTER_index[i]+1:ENTER_index[i+1]]))
else :
    hello += len(set(chat[ENTER_index[-1]+1:]))
print(hello)
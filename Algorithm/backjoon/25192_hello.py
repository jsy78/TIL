import sys

input = sys.stdin.readline

N = int(input())
chat = [input().rstrip() for _ in range(N)]
gomgom = set()
hello = 0

for i in range(N) :
    if chat[i] == 'ENTER' :
        for j in range(i+1, N) :
            if chat[j] != 'ENTER' :
                gomgom.add(chat[j])
            else :
                hello += len(gomgom)
                gomgom.clear()
                break
else :
    hello += len(gomgom)

print(hello)
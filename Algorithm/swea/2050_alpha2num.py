d = {}
cnt = 1
s = input()
for i in range(ord('A'), ord('Z')+1) :
    d[chr(i)] = cnt
    cnt += 1

for c in s :
    print(d[c], end=' ')

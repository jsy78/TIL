word = input()
dic = {}

for c in word :
    if dic.get(c.upper(), -1) == -1 :
        dic[c.upper()] = 1
    else :
        dic[c.upper()] += 1

max = max(dic.values())
alphabet = ''

if list(dic.values()).count(max) == 1 :
    for k in dic :
        if dic[k] == max :
            alphabet = k
            break
else :
    alphabet = '?'

print(alphabet)

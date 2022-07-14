word = 'banana'
dic = {}

for c in word :
    if dic.get(c, -1) == -1 :
        dic[c] = 1
    else :
        dic[c] += 1

for k, v in dic.items() :
    print(k, v)

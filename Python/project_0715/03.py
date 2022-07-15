fruit = {}
with open('data/fruits.txt', 'r', encoding='utf-8') as f :
    for line in f :
        newline = line.strip('\n')
        if fruit.get(newline, -1) == -1 :
            fruit[newline] = 1
        else :
            fruit[newline] += 1

with open('03.txt', 'w', encoding='utf-8') as f :
    for k, v in fruit.items() :
         f.write(f'{k} {v}\n')
berry = set()
with open('data/fruits.txt', 'r', encoding='utf-8') as f :
    text = f.read()
    # print(fruit, type(fruit))
    fruit = text.split('\n')
    # print(fruit, type(fruit))
    for name in fruit : 
        if name.endswith('berry') == True :
            berry.add(name)

# print(len(berry))
# print(berry)
with open('02.txt', 'w', encoding='utf-8') as f :
    f.write(f'{len(berry)}\n')
    for i in range(len(berry)) :
        f.write(f'{berry.pop()}\n')
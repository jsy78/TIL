with open('data/fruits.txt', 'r', encoding='utf-8') as f :
    text = f.read()
    # print(fruit, type(fruit))
    fruit = text.split('\n')
    # print(fruit, type(fruit))
    print(len(fruit))
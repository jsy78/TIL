with open('00.txt', 'w', encoding='utf-8') as f :
    f.write('3회차 조성윤\n')
    f.write('Hello, Python!\n')
    for i in range(5) :
        f.write(f'{i + 1}일차 파이썬 공부 중\n')
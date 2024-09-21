import sys
sys.stdin = open('7675_이름세기.txt', 'r')

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    data = input()
    while True :
        n = 0
        for c in data :
            if c in '.?!' :
                n += 1
        if n == N :
            break
        else :
            data += input().strip('\n')

    data = data.replace('.', '-').replace('?', '-').replace('!', '-')
    sentence = data.split('-')
    sentence.pop()
    for i in range(len(sentence)) :
        sentence[i] = sentence[i].split()

    result = []
    for lst in sentence :
        name = 0
        for word in lst :
            if word[0].isupper() and word[0].isalpha() :
                if word[1:].islower() and word[1:].isalpha() or word[1:] == '':
                    name += 1
        result.append(name)
    
    print(f'#{test_case}', *result)
code = {'0001101' : 0,
        '0011001' : 1,
        '0010011' : 2, 
        '0111101' : 3, 
        '0100011' : 4, 
        '0110001' : 5,
        '0101111' : 6, 
        '0111011' : 7,
        '0110111' : 8, 
        '0001011' : 9}

T = int(input())
for test_case in range(1, T+1) :
    N, M = map(int, input().split())
    original = [input() for _ in range(N)]
    abstract = []
    for line in original :
        if line.count('0') == len(line) :
            continue
        else :
            tmp = line.rstrip('0')
            while len(tmp) != 56 :
                tmp = tmp.replace('0', '', 1)
            abstract.append(tmp)
            
    password = abstract[0]
    convert = [code[password[i:i+7]] for i in range(0, 56, 7)]
    
    if ((sum(convert[i] for i in range(8) if i%2 == 0)) * 3 \
         + sum(convert[i] for i in range(8) if i%2 == 1)) % 10 == 0 :
        print(f'#{test_case} {sum(convert)}')
        # print(f'#{test_case} {sum(map(lambda s : s.count("1"), abstract))}')
    else :
        print(f'#{test_case} 0')
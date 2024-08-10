T = int(input())
for test_case in range(1, T+1) :
    string = input()
    for i in range(1, 10) :
        if string[0:i] == string[i:i*2] :
            print(f'#{test_case} {i}')
            break
    
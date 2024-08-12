lst = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']
for test_case in range(1, 11) :
    N, string = input().split()
    N = int(N)

    while True :
        for i in range(len(lst)) :
            if lst[i] in string :
                string = string.replace(lst[i], '')
                break
        else :
            break
    print(f'#{test_case} {string}')
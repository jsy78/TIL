lst_1 = ['01', '03', '05', '07', '08', '10', '12']
lst_2 = ['04', '06', '09', '11']
lst_3 = ['02']

T = int(input())
for test_case in range(1, T+1) :
    valid = False
    string = input()
    if string[4:6] in lst_1 and 1 <= int(string[6:]) <= 31 :
        valid = True
    elif string[4:6] in lst_2 and 1 <= int(string[6:]) <= 30 :
        valid = True
    elif string[4:6] in lst_3 and 1 <= int(string[6:]) <= 28 :
        valid = True
    
    if valid :
        print(f'#{test_case} {string[0:4]}/{string[4:6]}/{string[6:]}')
    else :
        print(f'#{test_case} -1')
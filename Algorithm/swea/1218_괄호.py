import sys
sys.stdin = open('1218_괄호.txt', 'r')

for test_case in range(1, 11) : 
    N = int(input())
    string = input()

    for _ in string :
        while '()' in string :
            string = string.replace('()', '')
        while '[]' in string :
            string = string.replace('[]', '')
        while '{}' in string :
            string = string.replace('{}', '')
        while '<>' in string :
            string = string.replace('<>', '')
    
    if len(string) == 0 :
        print(f'#{test_case} 1')
    else :
        print(f'#{test_case} 0')

sys.stdin.close()
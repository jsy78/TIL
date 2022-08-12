import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
for test_case in range(1, T+1) :
    S = input()
    S = S.replace('a', '')
    S = S.replace('e', '')
    S = S.replace('i', '')
    S = S.replace('o', '')
    S = S.replace('u', '')
    print(f'#{test_case} {S}')

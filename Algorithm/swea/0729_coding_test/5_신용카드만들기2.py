import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())

for test_case in range(1, T+1) :
    number_string = input()
    possible = 0

    if number_string.count('-') > 0 : # 문자열에 '-'가 있으면
        number_string = number_string.replace('-', '') # '-'를 지운다
    if len(number_string) == 16 : # 16자리인가?
        if number_string[0] in '34569' : # 16자리라면 첫번째 숫자가 3, 4, 5, 6, 9 중 하나인가?
            possible = 1

    print(f'#{test_case} {possible}')
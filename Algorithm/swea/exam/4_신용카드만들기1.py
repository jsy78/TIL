import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())

for test_case in range(1, T+1) :
    number = list(map(int, input().split()))
    # 1 2 3 4 5 6 7 8 9 : 사람이 인식하는 자리
    # 0 1 2 3 4 5 6 7 8 : 컴퓨터가 인식하는 인덱스
    even_sum = 0
    odd_sum = 0
    for i in range(15) :
        if (i+1) % 2 == 1 : # 홀수 자리
            odd_sum += (number[i]*2)
        else : # 짝수 자리
            even_sum += number[i]

    for N in range(0, 10) :
        if (odd_sum + even_sum + N) % 10 == 0 :
            print(f'#{test_case} {N}')
            break

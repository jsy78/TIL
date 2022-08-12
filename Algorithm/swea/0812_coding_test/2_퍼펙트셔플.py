from random import shuffle
import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    card = input().split()
    shuffle = []
    if N % 2 == 0 : 
        card_split_1 = card[0:N//2]
        card_split_2 = card[N//2:N]
        for i in range(N//2) :
            shuffle.append(card_split_1[i])
            shuffle.append(card_split_2[i])
    else :
        card_split_1 = card[0:N//2+1]
        card_split_2 = card[N//2+1:N]
        for i in range(N//2) :
            shuffle.append(card_split_1[i])
            shuffle.append(card_split_2[i])
        shuffle.append(card_split_1[-1])

    print(f'#{test_case}', end=' ')
    print(*shuffle, end=' ')
    print()


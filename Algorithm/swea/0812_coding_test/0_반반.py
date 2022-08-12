import sys

sys.stdin = open("_반반.txt")

T = int(input())
for test_case in range(1, T+1) :
    S = input()
    for i in range(4) :
        if S.count(S[i]) != 2 :
            print(f'#{test_case} No')
            break
    else :
        print(f'#{test_case} Yes')

T = int(input())
for test_case in range(1, T+1) :
    S = list(input())
    L = len(S)
    H = int(input())
    pos = list(map(int, input().split()))

    for i in range(L+1) :
        S.insert(i*2, '')

    for p in pos :
        S[p*2] += '-'

    print(f'#{test_case} {"".join(S)}')
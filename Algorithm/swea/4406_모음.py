T = int(input())
for test_case in range(1, T+1) :
    S = input()
    for c in S :
        if c in 'aeiou' :
            S = S.replace(c, '')

    print(f'#{test_case} {S}')
T = int(input())
result = []
for test_case in range(1, T+1) :
    A, B, C, D = map(int, input().split())

    if A/B > C/D :
        result.append('ALICE')
    elif A/B == C/D :
        result.append('DRAW')
    else :
        result.append('BOB')

for i, r in enumerate(result, start=1) :
    print(f'#{i} {r}')
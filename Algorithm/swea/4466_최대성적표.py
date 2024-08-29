T = int(input())
for test_case in range(1, T+1) :
    N, K = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort(reverse=True)

    print(f'#{test_case} {sum(score[:K])}')
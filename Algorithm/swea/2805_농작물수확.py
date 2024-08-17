T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    for i, j, k in zip(range(N//2), range(N-1, N//2, -1), range(N//2, 0, -1)) :
        farm[i][:k] = [0]*k
        farm[i][-1:-(k+1):-1] = [0]*k
        farm[j][:k] = [0]*k
        farm[j][-1:-(k+1):-1] = [0]*k

    print(f'#{test_case} {sum(map(sum, farm))}')
    
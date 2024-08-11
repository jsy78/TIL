N, M = map(int, input().split())
two_dimen_list = []

for _ in range(N) :
    two_dimen_list.append(list(map(int, input().split())))

K = int(input())

for _ in range(K) :
    i, j, x, y = map(int, input().split())
    sum_ = 0
    for n in range(i-1, x) :
        for m in range(j-1, y) :
            sum_ += two_dimen_list[n][m]
    print(sum_)

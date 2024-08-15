point_num = {}
num_point = {}

k = 1
for n in range(1, 301) :
    for (i, j) in zip(range(1, n+1), range(n, 0, -1)) :
        point_num[(i, j)] = k
        num_point[k] = (i, j)
        k += 1

T = int(input())
for test_case in range(1, T+1) :
    p, q = map(int, input().split())
    print(f'#{test_case} {point_num[num_point[p][0]+num_point[q][0], num_point[p][1]+num_point[q][1]]}')
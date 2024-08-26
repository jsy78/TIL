T = int(input())
result = []
for test_case in range(1, T+1) :
    N = list(map(int, input()))
    while len(N) > 1 :
        N = list(map(int, str(sum(N))))
    result.append(N[0])

for i in range(T) :
    print(f'#{i+1} {result[i]}')
P = [1, 1, 1]
for i in range(2, 101) :
    P.append(P[i-2]+P[i-1])

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    print(f'#{test_case} {P[N-1]}')
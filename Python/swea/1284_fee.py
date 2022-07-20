T = int(input())

for i in range(1, T+1) :
    P, Q, R, S, W = map(int, input().split())

    A = W * P
    if W <= R :
        B = Q
    else :
        B = Q + (W-R)*S

    print(f'#{i} {A}') if A < B else print(f'#{i} {B}')
T = int(input())
for test_case in range(1, T+1) :
    N, M = map(int, input().split())
    A = set(input().split())
    B = set(input().split())
    print(f'#{test_case} {len(A & B)}')
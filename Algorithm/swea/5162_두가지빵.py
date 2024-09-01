# T = int(input())
# for test_case in range(1, T+1) :
#     A, B, C = map(int, input().split())
#     DP = []

#     for x, a in enumerate(range(0, C+1, A)) :
#         for y, b in enumerate(range(0, C+1, B)) :
#             if C >= a+b :
#                 DP.append((x, y))

#     print(f'#{test_case} {max(map(lambda x : x[0] + x[1], DP))}')

T = int(input())
for test_case in range(1, T+1) :
    A, B, C = map(int, input().split())
    print(f'#{test_case} {C//min(A, B)}')

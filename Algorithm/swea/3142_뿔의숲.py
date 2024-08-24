'''
a = 유니콘
b = 트윈혼

a + 2b = n (뿔)
a + b  = m (마리)

a = 2m-n
b = n-m
'''


T = int(input())
for test_case in range(1, T+1) :
    N, M = map(int, input().split())
    print(f'#{test_case} {2*M-N} {N-M}')

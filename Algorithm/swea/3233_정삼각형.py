'''
Sa = 3^(1/2) * (1/2) * A * (1/2) * A = 3^(1/2) * (1/4) * A^2
Sb = 3^(1/2) * (1/2) * B * (1/2) * B = 3^(1/2) * (1/4) * B^2

Sa / Sb = A^2 / B^2
'''

T = int(input())
for test_case in range(1, T+1) :
    A, B = map(int, input().split())
    print(f'#{test_case} {A**2//B**2}')
    

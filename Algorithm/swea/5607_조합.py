# https://onsil-thegreenhouse.github.io/programming/problem/2018/04/02/problem_combination/

def extended_euclidean(a, b) :
    if b == 0 :
        return (1, 0)
    q = a // b
    x, y = extended_euclidean(b, a%b)

    return (y, x-q*y)

T = int(input())
for test_case in range(1, T+1) :
    N, R = map(int, input().split())
    P = 1234567891

    factorial = [1] * (N+1)
    for i in range(2, N+1) :
        factorial[i] = (i * factorial[i-1]) % P

    denominator = (factorial[R]*factorial[N-R]) % P
    x, y = extended_euclidean(denominator, P)
    
    result = ((factorial[N]%P) * x%P) % P
    if result < 0 :
        result += P

    print(f'#{test_case} {result}')
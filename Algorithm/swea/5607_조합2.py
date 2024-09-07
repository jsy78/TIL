# https://onsil-thegreenhouse.github.io/programming/problem/2018/03/29/problem_math_power/
# https://onsil-thegreenhouse.github.io/programming/problem/2018/04/02/problem_combination/
# https://m.blog.naver.com/hongjg3229/221650178981

def calcPow(a, n) :
    if n == 0 :
        return 1
    else :
        temp = calcPow(a, n//2)
        if n % 2 == 0 :
            return (temp*temp) % P
        else :
            return (temp*temp*a) % P
        
T = int(input())
for test_case in range(1, T+1) :
    N, R = map(int, input().split())
    P = 1234567891

    factorial = [1] * (N+1)
    for i in range(2, N+1) :
        factorial[i] = (i * factorial[i-1]) % P

    denominator = (factorial[R]*factorial[N-R]) % P

    result = ((factorial[N]%P) * calcPow(denominator, P-2)) % P

    print(f'#{test_case} {result}')
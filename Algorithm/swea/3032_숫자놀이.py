# 확장된 유클리드 알고리즘
# https://baeharam.github.io/posts/algorithm/extended-euclidean/
# https://velog.io/@cjy/nkryvnjc
# https://www.baeldung.com/cs/extended-euclidean-algorithm
# https://namnamseo.tistory.com/entry/GCD-Extended-Euclidean-Algorithm

def gcd(a, b) :
    if b == 0 :
        return a
    return gcd(b, a%b)

def extended_euclidean_recursive(a, b) :
    if b == 0 :
        return (a, 1, 0)
    q = a // b
    d, x, y = extended_euclidean_recursive(b, a%b)

    return (d, y, x-q*y)

def extended_euclidean_iterative(a, b) :
    x1, y1 = 1, 0 # a*1 + b*0 = a
    x2, y2 = 0, 1 # a*0 + b*1 = b

    while a%b > 0 :
        q = a // b
        x = x1 - q*x2
        y = y1 - q*y2

        x1, x2 = x2, x
        y1, y2 = y2, y

        a, b = b, a%b

    d = b

    return (d, x, y)

T = int(input())
for test_case in range(1, T+1) :
    A, B = map(int, input().split())
    d, x, y = extended_euclidean_iterative(A, B)
    if d != 1 :
        print(f'#{test_case} -1')
    else :
        print(f'#{test_case} {x} {y}')
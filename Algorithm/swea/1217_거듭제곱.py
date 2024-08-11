def pow(a: int, b: int, c: int = 1) -> int :
    if b == c :
        return a
    else :
        return a * pow(a, b, c+1)

for _ in range(1, 11) :
    test_case = int(input())
    A, B = map(int, input().split())
    print(f'#{test_case} {pow(A, B)}')
def prime_list(N) :
    sieve = [True] * (N+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(N**0.5)+1) :
        if sieve[i] == True :
            for j in range(i*2, N+1, i) :
                sieve[j] = False

    return [i for i in range(2, N+1) if sieve[i] == True]

prime = prime_list(10**6)

T = int(input())
for test_case in range(1, T+1) :
    D, A, B = map(int, input().split())
    sub_prime = [str(n) for n in prime if (A <= n <= B)]
    special_prime = [s for s in sub_prime if str(D) in s]
    print(f'#{test_case} {len(special_prime)}')
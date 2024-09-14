def prime_list(N) :
    sieve = [True] * (N+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(N**0.5)+1) :
        if sieve[i] == True :
            for j in range(i*2, N+1, i) :
                sieve[j] = False

    return [i for i in range(2, N+1) if sieve[i] == True]

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    prime = prime_list(N)
    result = 0
    for i in range(0, len(prime)) :
        for j in range(i, len(prime)) :
            for k in range(j, len(prime)) :
                if prime[i]+prime[j]+prime[k] == N :
                    result += 1
    
    print(f'#{test_case} {result}')

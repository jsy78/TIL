from math import sqrt

def prime_list(N) :
    sieve = [True] * (N+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(sqrt(N))+1) :
        if sieve[i] == True :
            for j in range(i*2, N+1, i) :
                sieve[j] = False

    return [i for i in range(2, N+1) if sieve[i] == True]

for n in prime_list(1000000) :
    print(n, end=' ')
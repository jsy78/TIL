T = int(input())

for i in range(1, T+1) :
    test_case = int(input())
    num_set = set()
    N = 0
    while len(num_set) != 10 :
        N += test_case
        num_str = str(N)
        for c in num_str :
            num_set.add(c)
    print(f'#{i} {N}')

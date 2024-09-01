T = int(input())
for test_case in range(1, T+1) :
    people = list(map(int, input()))
    employee = 0
    clap = 0

    for i, p in enumerate(people) :
        if clap < i :
            employee += (i-clap)
            clap += 1
        clap += p
    print(f'#{test_case} {employee}')
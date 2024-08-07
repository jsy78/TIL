T = int(input())
for test_case in range(1, T+1) : 
    n = int(input())
    number = list(map(int, input().split()))
    counter = dict()

    for num in number :
        if num not in counter :
            counter[num] = 1
        else :
            counter[num] += 1

    max_value = max(counter.values())
    max_list = list()

    for key, value in counter.items() :
        if value == max_value :
            max_list.append(key)
    print(f'#{n} {max(max_list)}')

def bonus(lst : list) -> int :
    return int(''.join(map(str, lst)))

def exchange(lst : list, v : list, l : int, cnt : int) -> None :
    global max_num

    if cnt == 0 :
        max_num = max(max_num, bonus(lst))
        return

    for i in range(l) :
        for j in range(i+1, l) :
            lst[i], lst[j] = lst[j], lst[i]
            temp = bonus(lst)
            if (cnt, temp) not in v :
                v.append((cnt, temp))
                exchange(lst, v, l, cnt-1)
            lst[i], lst[j] = lst[j], lst[i]

T = int(input())
for test_case in range(1, T+1) :
    number, swap = input().split()
    number = list(map(int, number))
    swap = int(swap)
    visited = list()
    max_num = 0
    
    exchange(number, visited, len(number), swap)
    print(f'#{test_case} {max_num}')
    
    
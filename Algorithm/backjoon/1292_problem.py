def seq_sum(x : int) -> int :
    num = 1
    plus_count = 0
    num_conut = 0
    one_to_x_sum = 0
    while plus_count < x : 
        one_to_x_sum += num
        plus_count += 1
        num_conut += 1
        if num_conut == num :
            num += 1
            num_conut = 0

    return one_to_x_sum

one2start, one2end = map(int, input().split())

print(seq_sum(one2end)-seq_sum(one2start-1))
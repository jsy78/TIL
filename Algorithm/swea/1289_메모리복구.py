T = int(input())
for test_case in range(1, T+1) :
    memory = list(map(int, input()))
    clear = [0] * len(memory)
    result = 0

    for i in range(len(memory)) :
        if memory[i] != clear[i] :
            result += 1
            for j in range(i, len(memory)) :
                clear[j] = memory[i]
    print(f'#{test_case} {result}')
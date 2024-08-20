import heapq

T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    heap = []
    result = []
    
    for _ in range(N) :
        calc = input()
        if ' ' in calc :
            push, node = map(int, calc.split())
            heapq.heappush(heap, (-node, node))
        else :
            pop = int(calc)
            if len(heap) != 0 :
                result.append(heapq.heappop(heap)[1])
            else :
                result.append(-1)

    print(f'#{test_case}', end=' ')
    for i in range(len(result)) :
        print(result[i], end=' ')
    print()
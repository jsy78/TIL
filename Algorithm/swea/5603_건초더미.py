T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    boxes = [int(input()) for _ in range(N)]
    count = 0
    avg = sum(boxes) // len(boxes)

    for i in range(N) :
        if boxes[i] > avg :
            count += boxes[i]-avg

    print(f'#{test_case} {count}')
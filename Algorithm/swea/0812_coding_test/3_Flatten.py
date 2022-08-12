import sys

sys.stdin = open("_Flatten.txt")

for test_case in range(1, 11) :
    N = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(N) :
        boxes[boxes.index(min(boxes))] += 1
        boxes[boxes.index(max(boxes))] -= 1
    
    print(f'#{test_case} {max(boxes)-min(boxes)}')
    
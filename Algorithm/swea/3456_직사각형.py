T = int(input())
for test_case in range(1, T+1) :
    rect = list(map(int, input().split()))

    for l in range(3) :
        if rect.count(rect[l]) == 1 or rect.count(rect[l]) == 3: # 직사각형의 나머지 한 변 or 정사각형
            print(f'#{test_case} {rect[l]}')
            break
        elif rect.count(rect[l]) == 2 :
            continue
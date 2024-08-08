T = int(input())
for test_case in range(1, T+1) :
    N = int(input())
    distance = 0
    speed = 0
    for _ in range(N) :
        try :
            command, acc = map(int, input().split())
        except ValueError :
            command = 0
            
        if command == 0 :
            distance += speed
        elif command == 1 :
            speed += acc
            distance += speed
        elif command == 2 :
            speed -= acc
            if speed < 0 :
                speed = 0
            distance += speed
    print(f'#{test_case} {distance}')
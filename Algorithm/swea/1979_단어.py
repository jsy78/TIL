T = int(input())
for test_case in range(1, T+1) :
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N) :
        word_len = 0
        for j in range(N) :
            if puzzle[i][j] == 1 :
                word_len += 1
            if puzzle[i][j] == 0 or j == N-1 :
                if word_len == K :
                    result += 1
                word_len = 0

    for i in range(N) :
        word_len = 0
        for j in range(N) :
            if puzzle[j][i] == 1 :
                word_len += 1
            if puzzle[j][i] == 0 or j == N-1 :
                if word_len == K :
                    result += 1
                word_len = 0

    print(f'#{test_case} {result}')
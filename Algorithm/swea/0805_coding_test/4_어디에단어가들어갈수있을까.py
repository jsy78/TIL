import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

T = int(input())

for test_case in range(1, T+1) :
    matrix_len, word_len = map(int, input().split())
    matrix = [''.join(input().split()) for _ in range(matrix_len)]
    # 주어진 입력값을 하나의 문자열로 만들어 저장 (input 가로 탐색 용)
    matrix_T = [''.join([matrix[i][j] for i in range(matrix_len)]) for j in range(matrix_len)]
    # matrix을 전치시켜 하나의 문자열로 만들어 저장 (input 세로 탐색 용)

    row_count = 0 
    for i in range(matrix_len) : # 가로 탐색
        matrix_split = matrix[i].split('0') # 0을 기준으로 문자열 분리
        for w in matrix_split :
            if len(w) == word_len :
                row_count += 1 
                # 0을 기준으로 분리한 문자열 리스트의 요소 길이가 단어 길이와 같으면 1 증가
    
    col_count = 0
    for i in range(matrix_len) : # 세로 탐색
        matrix_T_split = matrix_T[i].split('0') # 0을 기준으로 문자열 분리
        for w in matrix_T_split :
            if len(w) == word_len :
                col_count += 1
                # 0을 기준으로 분리한 문자열 리스트의 요소 길이가 단어 길이와 같으면 1 증가
    
    print(f'#{test_case} {row_count+col_count}')
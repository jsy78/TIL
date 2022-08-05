import sys

sys.stdin = open("_조교의성적매기기.txt")

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
        # 0     1     2     3     4     5     6     7     8     9

T = int(input())

for test_case in range(1, T+1) :
    student_num, curious_student = map(int, input().split())
    curious_student -= 1 # 컴퓨터용 인덱스로 변환
    score_list = []
    sorted_score_list = []
    for i in range(student_num) :
        mid, final, assignment = map(int, input().split())
        score_list.append((i, (mid*35 + final*45 + assignment*20)/100)) # 부동소수점 오차 방지

    sorted_score_list = sorted(score_list, key=lambda x: -x[1])
    # 학생의 번호와 점수를 대응시킨 튜플 리스트를 점수 내림차순 정렬
    
    for i in range(student_num) :
        if sorted_score_list[i] == score_list[curious_student] : # 확인할 학생 판별
            # print(i, student_num, score_list[curious_student], sorted_score_list[i]) # 중간 확인용
            for j in range(10) :
                if (student_num//10)*j <= i < (student_num//10)*(j+1) :
                    print(f'#{test_case} {grade[j]}')
            '''
            10명 grade index : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
            10명 score index : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
            (grade 요소가 1번 == 10//10번 반복)

            20명 grade index : 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5,  5,  6,  6,  7,  7,  8,  8,  9,  9
            20명 score index : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
            (grade 요소가 2번 == 20//10번 반복)
            
            30명 grade index : 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3,  3,  4,  4,  4,  5,  5,  5,  6,  6,  6,  7,  7,  7,  8,  8,  8,  9,  9,  9
            30명 score index : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29
            (grade 요소가 3번 == 30//10번 반복)
            '''
            
                    
                    
            


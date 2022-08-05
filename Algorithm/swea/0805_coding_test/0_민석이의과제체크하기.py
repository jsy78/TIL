import sys

sys.stdin = open("_민석이의과제체크하기.txt")

T = int(input())

for test_case in range(1, T+1) :
    all_student, submit_student = map(int, input().split())
    submit_student_list = list(map(int, input().split()))
    not_submit_student_list = [n for n in range(1, all_student+1) if n not in submit_student_list]
    # 제출한 목록에 없는 학생들의 리스트
    
    print(f'#{test_case} ', end='')
    for stu in not_submit_student_list :
        print(stu, end=' ')
    print()    
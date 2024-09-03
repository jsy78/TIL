T = int(input())
for test_case in range(1, T+1) :
    N, K = map(int, input().split())
    submit_student = list(map(int, input().split()))
    all_student = list(range(1, N+1))
    not_submit_student = [n for n in all_student if n not in submit_student]

    print(f'#{test_case}', end=' ')
    for stu in not_submit_student :
        print(stu, end=' ')
    print() 
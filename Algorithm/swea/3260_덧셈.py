from collections import deque

T = int(input())
for test_case in range(1, T+1) :
    A, B = input().split()
    A = list(map(int, A))
    B = list(map(int, B))
    C = deque()

    A_ptr = len(A)-1
    B_ptr = len(B)-1
    carry = 0

    while A_ptr >= 0 or B_ptr >= 0 :
        if A_ptr >= 0 and B_ptr >= 0 :
            temp = A[A_ptr] + B[B_ptr] + carry
            value = temp % 10
            carry = temp // 10

            C.appendleft(value)
            A_ptr -= 1
            B_ptr -= 1

        elif A_ptr >= 0 and B_ptr < 0 :
            temp = A[A_ptr] + carry
            value = temp % 10
            carry = temp // 10

            C.appendleft(value)
            A_ptr -= 1

        elif A_ptr < 0 and B_ptr >= 0 :
            temp = B[B_ptr] + carry
            value = temp % 10
            carry = temp // 10

            C.appendleft(value)
            B_ptr -= 1

    if carry > 0 :
        C.appendleft(carry)

    print(f'#{test_case}', end=' ')
    while C :
        print(C.popleft(), end='')
    print()

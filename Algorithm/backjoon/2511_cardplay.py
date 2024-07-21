import sys

input = sys.stdin.readline

A = list(map(int, input().split()))
B = list(map(int, input().split()))
WIN = list()
A_score = B_score = 0

for i in range(10) :
    if A[i] > B[i] :
        WIN.append('A')
        A_score += 3
    elif A[i] < B[i] :
        WIN.append('B')
        B_score += 3
    else :
        WIN.append('D')
        A_score += 1
        B_score += 1

print(A_score, B_score)

if A_score > B_score :
    print('A')
elif A_score < B_score :
    print('B')
else :
    for i in range(9, -1, -1):
        if WIN[i] == 'D' :
            continue
        else :
            print(WIN[i])
            break
    else :
        print('D')
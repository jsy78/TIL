score_list = []

for i in range(5) :
    A, B, C, D = map(int, input().split())
    score_list.append(A + B + C + D)

print(score_list.index(max(score_list))+1, max(score_list))
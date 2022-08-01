N, M = map(int, input().split())
book_num = []
book_list = []
possible = 1
for i in range(M) :
    book_num.append(int(input()))
    book_list.append(list(map(int, input().split())))
for i in range(M) :
    for j in range(book_num[i]-1) :
        if book_list[i][j] < book_list[i][j+1] :
            possible = 0
if possible == 1 :
    print('Yes')
else :
    print('No')
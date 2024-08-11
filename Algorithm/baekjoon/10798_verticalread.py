from sys import stdin

input = stdin.readline

lst = [list(input().strip()) for _ in range(5)]
max_len = max(map(len, lst))

# for i in range(max_len) :
#     for j in range(5) :
#         try :
#             print(lst[j][i], end='')
#         except IndexError :
#             continue

for i in range(max_len) :
    for j in range(5) :
        if i < len(lst[j]) :
            print(lst[j][i], end='')
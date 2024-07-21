import sys

sys.stdin = open('10816_numcard2.txt', 'r')
input = sys.stdin.readline

N = int(input())
own = list(map(int, input().split()))
M = int(input())
given = list(map(int, input().split()))

# for i in range(M) :
#     count = 0
#     for j in range(N) :
#         if given[i] == own[j] :
#             count += 1
#     print(count, end=' ')

dic = dict()
for i in range(M) :
    dic[given[i]] = 0

for j in range(N) :
    if dic.get(own[j], 'x') != 'x' :
        dic[own[j]] += 1

for v in range(M):
    print(dic[given[v]], end=' ')

sys.stdin.close()
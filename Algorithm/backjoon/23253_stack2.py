from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

book_num = 0
book_list = []
possible = True

for _ in range(M) :
    book_num = int(input())
    book_list.append(list(map(int, input().split())))

for book in book_list :
    if book != sorted(book, reverse=True) :
        possible = False

print('Yes') if possible else print('No')
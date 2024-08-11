from sys import stdin

input = stdin.readline

note = input().strip()

if note == '1 2 3 4 5 6 7 8' :
    print('ascending')
elif note == '8 7 6 5 4 3 2 1' :
    print('descending')
else :
    print('mixed')
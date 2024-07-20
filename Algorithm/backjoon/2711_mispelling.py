from sys import stdin

stdin = open('2711_mispelling.txt', 'r')
input = stdin.readline

T = int(input())
for _ in range(T):
    i, word = input().split()
    i = int(i)
    lst = list(word)
    lst.pop(i-1)
    print(''.join(lst))

stdin.close()
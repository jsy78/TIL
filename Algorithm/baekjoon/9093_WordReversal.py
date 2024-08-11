import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    sentence = input().split()
    for word in sentence :
        print(word[::-1], end=' ')
    print()
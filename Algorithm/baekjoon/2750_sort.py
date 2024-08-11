import sys

input = sys.stdin.readline

T = int(input())
numbers = []
for i in range(T) :
    numbers.append(int(input()))

numbers.sort()
for n in numbers:
    print(n)
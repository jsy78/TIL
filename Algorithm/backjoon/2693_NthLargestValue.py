import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    array = list(map(int, input().split()))
    array.sort(reverse=True)
    print(array[2])
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    zero_count = 0
    N, M = map(int, input().split())
    paper = map(str, range(N, M+1))
    for number in paper :
        zero_count += number.count('0')
    print(zero_count)
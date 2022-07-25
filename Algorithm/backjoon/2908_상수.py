# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("2908_상수.txt")

A, B = map(int, input().split())

str_A = str(A)
str_B = str(B)

reverse_A = int(str_A[::-1])
reverse_B = int(str_B[::-1])

print(reverse_A) if reverse_A > reverse_B else print(reverse_B)
# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("2577_숫자의개수.txt")

A = int(input())
B = int(input())
C = int(input())

string = str(A*B*C)
num_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for char in string :
    num_list[int(char)] += 1

for num in num_list :
    print(num)
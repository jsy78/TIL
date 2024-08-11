# https://www.acmicpc.net/problem/10818

from sys import stdin

N = int(stdin.readline())
num_list = list(map(int, stdin.readline().split()))

print(min(num_list), max(num_list))
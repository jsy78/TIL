# https://www.acmicpc.net/problem/10952

from sys import stdin

stdin = open('10952_sum.txt', 'r')
input = stdin.readline

while True :
    a, b = map(int, input().split())
    if a+b == 0 :
        break
    print(f'{a + b}')
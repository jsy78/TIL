# https://www.acmicpc.net/problem/2753

Y = int(input())

print(1) if Y%4 == 0 and Y%100 != 0 or Y%400 == 0 else print(0)
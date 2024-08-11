from sys import stdin
input = stdin.readline

N = int(input())
store = list(map(int, input().split()))

drink = 0
for i in range(N) : 
    if store[i] == drink % 3 :
        drink += 1

print(drink)
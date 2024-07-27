import sys

sys.stdin = open('15953_prizehunter.txt', 'r')
input = sys.stdin.readline

fes_2017 = {
    0 : 0,
    1 : 5000000,
    2 : 3000000,
    3 : 2000000,
    4 : 500000,
    5 : 300000, 
    6 : 100000
}

fes_2018 = {
    0 : 0,
    1 : 5120000,
    2 : 2560000, 
    3 : 1280000,
    4 : 640000,
    5 : 320000
}

T = int(input())
for _ in range(T) :
    a, b = map(int, input().split())

    if a == 1 :
        a = 1
    elif 2 <= a <= 3 :
        a = 2
    elif 4 <= a <= 6 :
        a = 3
    elif 7 <= a <= 10 :
        a = 4
    elif 11 <= a <= 15 :
        a = 5
    elif 16 <= a <= 21 :
        a = 6
    else :
        a = 0

    if b == 1 :
        b = 1
    elif 2 <= b <= 3 :
        b = 2
    elif 4 <= b <= 7 :
        b = 3
    elif 8 <= b <= 15 :
        b = 4
    elif 16 <= b <= 31 :
        b = 5
    else :
        b = 0

    print(fes_2017[a] + fes_2018[b])

sys.stdin.close()
import sys

input = sys.stdin.readline

def distance(a : int, b : int) -> int :
    vertical_dist = abs((a-1)%4 - (b-1)%4)
    if a % 4 == 0 and b % 4 != 0 :
        horizontal_dist = abs((a-4)//4 - (b-(b%4))//4)
    elif a % 4 != 0 and b % 4 == 0 :
        horizontal_dist = abs((a-(a%4))//4 - (b-4)//4) 
    elif a % 4 != 0 and b % 4 != 0 :
        horizontal_dist = abs((a-(a%4))//4 - (b-(b%4))//4)
    else :
        horizontal_dist = abs((a-4)//4 - (b-4)//4)

    return vertical_dist + horizontal_dist

a, b = map(int, input().split())
print(distance(a, b))
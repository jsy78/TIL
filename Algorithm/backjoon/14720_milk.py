from sys import stdin

input = stdin.readline

def drink(lst : list) -> int :
    visited = [False] * len(lst)
    pointer = 0

    while 0 <= pointer < len(lst) :
        if 0 not in lst[pointer:] :
            pointer = -1
        else :
            pointer = lst.index(0, pointer)
            visited[pointer] = True
            if 1 not in lst[pointer:] :
                pointer = -1
            else:
                pointer = lst.index(1, pointer)
                visited[pointer] = True
                if 2 not in lst[pointer:] :
                    pointer = -1
                else :
                    pointer = lst.index(2, pointer)
                    visited[pointer] = True
    return sum(visited)

N = int(input())
shop = list(map(int, input().split()))

print(drink(shop))
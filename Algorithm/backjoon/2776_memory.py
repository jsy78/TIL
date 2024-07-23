import sys
input = sys.stdin.readline

def binary_search(lst, left, right, find) :
    if left > right :
        return 0
    
    mid = (left + right) // 2
    if lst[mid] < find :
        return binary_search(lst, mid+1, right, find)
    elif lst[mid] > find :
        return binary_search(lst, left, mid-1, find)
    else :
        return 1

T = int(input())

for _ in range(T) :
    N = int(input())
    note_1 = list(map(int, input().split()))
    M = int(input())
    note_2 = list(map(int, input().split()))

    note_1.sort()
    for m in note_2 :
        print(binary_search(note_1, 0, len(note_1)-1, m))


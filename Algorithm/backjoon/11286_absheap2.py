import heapq
import sys

sys.stdin = open('11286_absheap.txt', 'r')

T = int(input())

heap = []
for _ in range(T) :
    x = int(input())
    if x != 0 :
        heapq.heappush(heap, (abs(x), x))
    else :
        if len(heap) == 0 :
            print(0)
        else :
            print(heapq.heappop(heap)[1])
    
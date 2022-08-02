import heapq
import sys

sys.stdin = open('11286_absheap.txt', 'r')

T = int(input())

plus_heap = []
minus_heap = []
for i in range(T) :
    x = int(input())
    if x > 0 :
        heapq.heappush(plus_heap, x)
    elif x < 0 :
        heapq.heappush(minus_heap, abs(x))
    elif x == 0 :
        if len(plus_heap) == 0 and len(minus_heap) != 0 :
            print(-heapq.heappop(minus_heap))
        elif len(plus_heap) != 0 and len(minus_heap) == 0 :
            print(heapq.heappop(plus_heap))
        elif len(plus_heap) == 0 and len(minus_heap) == 0 :
            print(0)
        else :
            if minus_heap[0] <= plus_heap[0] :
                print(-heapq.heappop(minus_heap))
            else :
                print(heapq.heappop(plus_heap))
    
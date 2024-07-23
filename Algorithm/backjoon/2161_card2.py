from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
card_deque = deque(range(1, N+1))

for _ in range(N) :
    print(card_deque.popleft(), end=' ')
    if len(card_deque) == 0 :
        break
    card_deque.append(card_deque.popleft())
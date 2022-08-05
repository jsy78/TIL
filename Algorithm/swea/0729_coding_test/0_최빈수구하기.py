import sys
from collections import Counter
# 어제 배운 Counter 함수를 사용해봤음

sys.stdin = open("_최빈수구하기.txt")

T = int(input())

for i in range(1, T+1) :
    test_case = int(input())
    score = map(int, input().split())

    print(f'#{test_case} {sorted(Counter(score).most_common(), key=lambda x : (-x[1], -x[0]))[0][0]}')
    # .most_common() 메소드를 사용해 최빈값 순으로 출력 가능
    # 그리고 그걸 다시 점수 순으로 출력해야 함
    # 예전 실습 때 배웠던 sorted key와 lambda가 생각나서 활용해봤음
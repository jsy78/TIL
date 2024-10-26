import sys
sys.stdin = open('1486_높은선반.txt', 'r')

def solve(idx, end) :
    global min_height

    if sum(tower) >= B :
        min_height = min(min_height, sum(tower))
        return
    if idx == end :
        return
    tower.append(H[idx])
    solve(idx+1, end)
    tower.pop()
    solve(idx+1, end)

T = int(input())
for test_case in range(1, T+1) :
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    tower = []
    min_height = float('inf')
    
    solve(0, N)

    print(f'#{test_case} {min_height-B}')
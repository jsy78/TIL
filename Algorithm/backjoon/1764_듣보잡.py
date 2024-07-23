import sys

sys.stdin = open('1764_듣보잡.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
N_lst = [input().strip() for _ in range(N)]
M_lst = [input().strip() for _ in range(M)]

print(len(set(N_lst) & set(M_lst)))
for name in sorted(list(set(N_lst) & (set(M_lst)))) :
    print(name)

sys.stdin.close()
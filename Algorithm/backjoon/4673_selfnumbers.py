# https://www.acmicpc.net/problem/4673

num_list = list(range(1, 10001))
num_set = set(range(1, 10001))
not_self_set = set()

for num in num_list :
    not_self_set.add(num + sum(list(map(int, str(num)))))

self_set = num_set - not_self_set
self_num_list = list(self_set)
self_num_list.sort()
for n in self_num_list :
    print(n)
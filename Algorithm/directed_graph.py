from pprint import pprint

V, E = map(int, input().split())
adjacent_matrix = [[0]*(V+1) for _ in range(V+1)]
adjacent_list = [[] for _ in range(V+1)]

for _ in range(E) :
    v1, v2 = map(int, input().split())
    adjacent_matrix[v1][v2] = 1
    adjacent_list[v1].append(v2)

pprint(adjacent_matrix)
print(adjacent_list)
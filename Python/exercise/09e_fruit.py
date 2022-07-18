# from pprint import pprint

# fruits = [
#     "Soursop",
#     "Grapefruit",
#     "Apricot",
#     "Juniper berry",
#     "Feijoa",
#     "Blackcurrant",
#     "Cantaloupe",
#     "Salal berry",
# ]

# fruit_count = {}

# for fruit in fruits:
#     if fruit not in fruit_count:
#         fruit_count = {fruit: 1}
#     else:
#         fruit_count[fruit] += 1

# pprint(fruit_count)
# 딕셔너리에 키 값을 추가해야 하는데 계속 덮어씌워서 생기는 오류

from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)
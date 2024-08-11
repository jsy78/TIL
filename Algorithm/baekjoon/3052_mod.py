num_list = []
for n in range(10) :
    num_list.append(int(input()))

for i in range(10) :
    num_list[i] %= 42

print(len(set(num_list)))
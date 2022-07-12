number = [3, 10, 20]
len, sum = 0, 0

for i in number :
    len += 1
    sum += i

avg = int(sum / len)
print(avg)
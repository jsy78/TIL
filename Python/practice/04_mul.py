n = 5
i, sum = 1, 1
while i <= n :
    sum *= i
    i += 1
print(sum)

sum = 1
for i in range(n) :
    sum *= (i+1)
print(sum)


numbers = [0, 20, 100, 50, -60, 50, 100] # -30

#for i in range(len(numbers)) :
#    min = i
#    for j in range(i + 1, len(numbers)) :
#        if numbers[min] > numbers[j] :
#            min = j
#    numbers[i], numbers[min] = numbers[min], numbers[i]

for i in range(1, len(numbers)) :
    for j in range(i, 0, -1) : 
        if numbers[j] < numbers[j - 1] :
            numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]

second = 0
for i in range(len(numbers) - 1, -1, -1) :
    if numbers[i - 1] != numbers[i] :
        second = i - 1
        break

print(numbers[second])
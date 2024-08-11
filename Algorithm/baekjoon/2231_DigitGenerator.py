N = int(input())

digit_sum = 0

for num in range(1, N+1) :
    digit_list = list(map(int, str(num)))
    if num + sum(digit_list) == N :
        digit_sum = num
        break

print(digit_sum)
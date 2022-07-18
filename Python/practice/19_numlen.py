number = int(input())
cnt = 1
dec = 1
while dec > number or dec*10 <= number :
    cnt += 1
    dec *= 10
print(cnt)
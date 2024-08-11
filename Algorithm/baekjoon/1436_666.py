N = int(input())
list_666 = [0]
number = 666
cnt = 0
while len(list_666) < 20001 :
    num2str = str(number)
    for i in range(len(num2str)-1, 1, -1) :
        if num2str[i] == '6' and num2str[i-1] == '6' and num2str[i-2] == '6' :
            list_666.append(number)
            cnt += 1
            break
    if cnt == N :
        break
    number += 1
print(list_666[N])


N = int(input())
card_list = [n for n in range(1, N+1)]

for i in range(1, N+1) :
    if len(card_list) == 1 :
        break
    else :
        print(card_list.pop(0), end=' ')
        card_list.append(card_list.pop(0))
print(card_list[0])
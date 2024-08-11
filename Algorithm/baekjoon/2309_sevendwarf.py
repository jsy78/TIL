dwarf = [int(input()) for _ in range(9)]
one, two = 0, 0
flag = False
for i in range(0, 8) :
    if flag == True :
        break
    for j in range(i+1, 9) :
        if sum(dwarf) - (dwarf[i]+dwarf[j]) == 100 :
            one = dwarf[i]
            two = dwarf[j]
            flag = True
            break
dwarf.remove(one)
dwarf.remove(two)
dwarf.sort()
for d in dwarf :
    print(d)
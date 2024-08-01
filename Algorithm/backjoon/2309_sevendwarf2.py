import sys
input = sys.stdin.readline

dwarf = [int(input()) for _ in range(9)]
dwarf.sort()
dwarf_sum = sum(dwarf)
flag = False

for i in range(0, 9) :
    if flag == True :
        break
    for j in range(i+1, 9) :
        if dwarf[i]+dwarf[j] == dwarf_sum-100 :
            dwarf.pop(i)
            dwarf.pop(j-1) # 위에서 pop을 해가지고 인덱스 변화가 생김
            flag = True
            break
print(dwarf)
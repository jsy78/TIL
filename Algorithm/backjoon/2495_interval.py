import sys
input = sys.stdin.readline

for _ in range(3) :
    string = input().rstrip()
    prev_c = '0'
    count = 1
    count_list = []
    for c in string :
        if c == prev_c :
            count += 1
        else :
            count_list.append(count)
            count = 1
        prev_c = c
    else :
        count_list.append(count)
        count = 1
        
    print(max(count_list))

    prev_c = '0'
    count = 1
    count_list.clear()
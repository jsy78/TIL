N = int(input())
Pi = list(map(int, input().split()))
sub_Pi = []
height = 0
jump = -1

for i in range(N-1) :
    if i < jump :
        continue
    
    if Pi[i] < Pi[i+1] :
        for j in range(i, N) :
            sub_Pi.append(Pi[j])
            jump = j
            if len(sub_Pi) < 2 :
                continue
            else :
                if sub_Pi[len(sub_Pi)-2] >= sub_Pi[len(sub_Pi)-1] :
                    sub_Pi.pop(len(sub_Pi)-1)
                    break

        if height < max(sub_Pi)-min(sub_Pi) :
            height = max(sub_Pi)-min(sub_Pi)

        sub_Pi.clear()

print(height)
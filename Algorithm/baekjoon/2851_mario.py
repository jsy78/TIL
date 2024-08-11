mushroom = []
for i in range(10) :
    mushroom.append(int(input()))

prefix_sum = []
score_sum = 0
for score in mushroom :
    score_sum += score
    prefix_sum.append(score_sum)
    if score_sum >= 100 :
        break

semi_final = prefix_sum[len(prefix_sum)-2]
final = prefix_sum[len(prefix_sum)-1] 
result = final if abs(final-100) <= abs(semi_final-100) else semi_final 
print(result)
    

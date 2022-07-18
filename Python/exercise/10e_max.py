# number_list = [1, 23, 9, 6, 91, 59, 29]
# max = max(number_list)

# number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
# max2 = max(number_list2)

# if max > max2:
#     print("첫 번째 리스트의 최댓값이 더 큽니다.")

# elif max < max2:
#     print("두 번째 리스트의 최댓값이 더 큽니다.")

# else:
#     print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")
# 변수의 이름으로 내장 함수의 이름을 사용해서는 안됨

number_list = [1, 23, 9, 6, 91, 59, 29]
max1 = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max1 > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max1 < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")
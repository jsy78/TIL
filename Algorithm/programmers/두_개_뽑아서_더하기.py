# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    
    answer.sort()
    idx = 0
    while idx < len(answer) :
        if answer.count(answer[idx]) > 1 :
            answer.pop(idx)
        else :
            idx += 1

    return answer

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))

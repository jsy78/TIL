# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("8958_OX퀴즈.txt")

T = int(input())

for i in range(1, T+1) :
    quiz_result = input()
    score_result = 0
    score = 0

    for quiz in quiz_result :
        if quiz == 'O' :
            score += 1
        else :
            score = 0
        score_result += score

    print(score_result)

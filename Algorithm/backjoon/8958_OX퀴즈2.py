# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("8958_OX퀴즈.txt")

T = int(input())

for _ in range(T) :
    quiz = input()
    
    correct_list = quiz.split('X')
    total = 0
    for correct in correct_list :
        n = len(correct)
        
        score = (n * (n+1)) / 2
        total += score

    print(int(total))
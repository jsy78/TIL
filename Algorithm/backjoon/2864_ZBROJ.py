import sys
input = sys.stdin.readline

A, B = input().split()

A_SixToFive = A.replace('6', '5')
B_SixToFive = B.replace('6', '5')

A_FiveToSix = A.replace('5', '6')
B_FiveToSix = B.replace('5', '6')

print(int(A_SixToFive) + int(B_SixToFive), int(A_FiveToSix) + int(B_FiveToSix))
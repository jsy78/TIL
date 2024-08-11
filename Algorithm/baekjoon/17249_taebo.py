import sys
input = sys.stdin.readline

S = input()

# S = S.replace('=', '')

print(S[:S.find('(')].count('@'), S[S.find(')')+1:].count('@'))
import sys
input = sys.stdin.readline

censor = 'CAMBRIDGE'
word = input()

for c in word :
    if c in censor :
        word = word.replace(c, '')

print(word)
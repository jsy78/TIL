import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    word1, word2 = input().split()
    if sorted(word1) == sorted(word2) :
        print(f'{word1} & {word2} are anagrams.')
    else :
        print(f'{word1} & {word2} are NOT anagrams.')
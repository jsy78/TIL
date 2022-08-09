from sys import stdin
from collections import Counter

stdin = open('1371_char.txt', 'r')
input = stdin.read

s = input().replace("\n","").replace(" ","")
list_ = Counter(s).most_common()
char = []
freq = []
for c, f in list_ :
    freq.append(f)

for i in range(freq.count(freq[0])) :
    char.append(list_[i][0])

char.sort()
print(*char, sep='')
import sys
input = sys.stdin.readline

string = input().strip()

while not string.isupper() :
    for s in string :
        if ord(s) == 45 or ord(s) >= 97 :
            string = string.replace(s, '')

print(string)
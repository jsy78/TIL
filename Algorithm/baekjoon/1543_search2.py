import sys
input = sys.stdin.readline

document = input().rstrip()
search_keyword = input().rstrip()
count = 0

while search_keyword in document :
    document = document.replace(search_keyword, '*', 1)
    count += 1
    
print(count)
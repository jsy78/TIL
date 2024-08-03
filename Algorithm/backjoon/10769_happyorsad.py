import sys
input = sys.stdin.readline

message = input()

happy = message.count(':-)')
sad = message.count(':-(')

if happy == 0 and sad == 0 :
    print('none')
else :
    if happy > sad :
        print('happy')
    elif happy < sad :
        print('sad')
    else :
        print('unsure')
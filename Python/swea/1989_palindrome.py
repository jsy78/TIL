T = int(input())

for i in range(1, T+1) :
    word = input()
    print(f'#{i} {int(word == word[::-1])}')
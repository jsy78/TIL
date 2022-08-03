N = int(input())
numbers = [[], [], []]
scores = [0] * N

for _ in range(N) :
    a, b, c = map(int, input().split())
    numbers[0].append(a)
    numbers[1].append(b)
    numbers[2].append(c)

for i in range(3) :
    for j in range(N) :
        if numbers[i].count(numbers[i][j]) >= 2 :
            scores[j] += 0
        else :
            scores[j] += numbers[i][j]

for s in scores :
    print(s)
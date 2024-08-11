N, M = map(int, input().split())
card = list(map(int, input().split()))
sum_, max_ = 0, 0
for i in range(0, N-2) :
    for j in range(i+1, N-1) :
        for k in range(j+1, N) :
            sum_ = card[i] + card[j] + card[k]
            if max_ < sum_ < M :
                max_ = sum_
            elif sum_ == M :
                max_ = sum_
                break
            elif sum_ > M :
                continue
print(max_)

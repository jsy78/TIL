num2word = {0:"ZRO", 1:"ONE", 2:"TWO", 3:"THR", 4:"FOR", 5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"}
word2num = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
T = int(input())
for _ in range(T) :
    test_case, N = map(int, input().lstrip('#').split())
    word = input().split()
    num = [word2num[word[i]] for i in range(N)]
    num.sort()
    sorted_word = [num2word[num[i]] for i in range(N)]
    print(f'#{test_case}')
    print(*sorted_word, sep=' ')    

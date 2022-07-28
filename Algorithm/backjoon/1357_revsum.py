def Rev(x : int) -> int :
    num_to_str = str(x)
    return int(num_to_str[::-1])

X, Y = map(int, input().split())
print(Rev(Rev(X) + Rev(Y)))

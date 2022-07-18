# numbers = input().split()
# print(sum(numbers))
# input은 기본적으로 str 타입이므로
# int로 변환해야 함

numbers = map(int, input().split())
print(sum(numbers))
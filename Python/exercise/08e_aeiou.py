# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)
# 모음 하나마다 따로 연산을 해줘야 함

word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char ==  "i" or char == "o" or char == "u":
        count += 1

print(count)

# word = "HappyHacking"

# count = 0

# for char in word:
#     if char in "aeiou":
#         count += 1

# print(count)
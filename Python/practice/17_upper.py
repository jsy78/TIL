word = 'banana'
new_word = ''

for c in word :
    if 97 <= ord(c) <= 122 :
        new_word += chr(ord(c) - 32)

print(new_word)
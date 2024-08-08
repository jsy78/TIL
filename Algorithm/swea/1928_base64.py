def base64_encoder(string : str) -> str :
    base64_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    buffer = ''.join([bin(ord(char))[2:].zfill(8) for char in string])
    return ''.join([base64_table[int(buffer[i:i+6], 2)] for i in range(0, len(buffer), 6)])

def base64_decoder(string : str) -> str :
    base64_table = {char : i for i, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')}
    buffer = ''.join([bin(base64_table[char])[2:].zfill(6) for char in string])
    return ''.join([chr(int(buffer[i:i+8], 2)) for i in range(0, len(buffer), 8)])

T = int(input())
for test_case in range(1, T+1) :
    string = input()
    print(f'#{test_case} {base64_decoder(string)}')
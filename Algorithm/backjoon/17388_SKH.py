import sys
input = sys.stdin.readline

S, K, H = map(int, input().split())
if S + K + H >= 100 :
    print('OK')
else :
    if min(S, K, H) == S :
        print('Soongsil')
    elif min(S, K, H) == K :
        print('Korea')
    elif min(S, K, H) == H :
        print('Hanyang')
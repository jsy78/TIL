T = int(input())

for i in range(1, T+1) :
    h1, m1, h2, m2 = map(int, input().split())
    
    h3 = h1 + h2
    m3 = m1 + m2

    if m3 > 59 :
        m3 -= 60
        h3 += 1
    while h3 > 12 : # 6:00 + 6:00 == 12:00 
        h3 -= 12    # 12:59 + 12:59 == 25:58 == 1:58 

    print(f'#{i} {h3} {m3}')
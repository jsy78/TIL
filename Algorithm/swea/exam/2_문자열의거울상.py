import sys

sys.stdin = open("_문자열의거울상.txt")

dict_bdpq = {
    'b' : 'd',
    'd' : 'b',
    'p' : 'q',
    'q' : 'p'
}

T = int(input())

for i in range(1, T+1) :
    string = input()
    reverse_string = string[::-1] # 인덱스 역순으로 뒤집기
    mirror_string = []

    for c in reverse_string :
        mirror_string.append(dict_bdpq[c]) # 딕셔너리를 참조해 추가

    print(f'#{i} {"".join(mirror_string)}') # 추가한 문자들을 join을 통해 하나로 합침
                # 이미 작은따옴표로 묶어버려서 큰따옴표를 사용
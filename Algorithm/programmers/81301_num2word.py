def solution(s):
    word_to_num = {
        'zero'  : '0',
        'one'   : '1',
        'two'   : '2',
        'three' : '3',
        'four'  : '4',
        'five'  : '5',
        'six'   : '6',
        'seven' : '7',
        'eight' : '8',
        'nine'  : '9'
    }
    for k in word_to_num :
        s = s.replace(k, word_to_num[k])
    return int(s)
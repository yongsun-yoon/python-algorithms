# https://school.programmers.co.kr/learn/courses/30/lessons/131128

from collections import Counter

def solution(X, Y):
    cnt_x = Counter(X)
    cnt_y = Counter(Y)
    commons = cnt_x & cnt_y
    commons = sorted(commons.items(), reverse=True)
    if not commons:
        return '-1'
    
    answer = ''
    for k, v in commons:
        answer += str(k) * v
        
    if answer[0] == '0':
        answer = '0'

    return answer

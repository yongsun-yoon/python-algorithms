# https://school.programmers.co.kr/learn/courses/30/lessons/120891

def solution(order):
    answer = 0
    for o in str(order):
        if o in ['3', '6', '9']:
            answer += 1
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    answer = 0
    for _a, _b in zip(a, b):
        answer += _a * _b
    return answer

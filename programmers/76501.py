# https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0
    for a, s in zip(absolutes, signs):
        s = 1 if s else -1
        answer += a * s
    return answer

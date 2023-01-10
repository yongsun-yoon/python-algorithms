# https://school.programmers.co.kr/learn/courses/30/lessons/147355


def solution(t, p):
    lt = len(t)
    lp = len(p)

    answer = 0
    for i in range(0, lt-lp+1):
        if t[i:i+lp] <= p:
            answer += 1

    return answer
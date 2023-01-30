# https://school.programmers.co.kr/learn/courses/30/lessons/138477

from bisect import bisect

def solution(k, score):
    answer = []
    hof = []
    for s in score:
        if len(hof) < k:
            idx = bisect(hof, s)
            hof.insert(idx, s)
        else:
            if s > hof[0]:
                hof.pop(0)
                idx = bisect(hof, s)
                hof.insert(idx, s)
        answer.append(hof[0])
                
    return answer

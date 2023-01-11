# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    addr = {}

    answer = []
    for i, c in enumerate(s):
        prev = addr.get(c, None)
        dist = -1 if prev is None else i - prev
        answer.append(dist)
        addr[c] = i
    
    return answer
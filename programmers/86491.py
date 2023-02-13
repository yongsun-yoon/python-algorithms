# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    maxl, maxs = 0, 0
    for size in sizes:
        l, s = sorted(size)
        if l > maxl:
            maxl = l
        if s > maxs:
            maxs = s
    
    answer = maxl * maxs
    return answer

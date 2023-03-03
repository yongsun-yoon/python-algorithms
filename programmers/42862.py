# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    reserve = set(reserve)
    lost = set(lost)
    
    common = reserve & lost
    reserve -= common
    lost -= common
    
    for r in reserve:
        prev, post = r-1, r+1
        if prev in lost:
            lost.remove(prev)
        elif post in lost:
            lost.remove(post)
    
    answer = n - len(lost)
    return answer

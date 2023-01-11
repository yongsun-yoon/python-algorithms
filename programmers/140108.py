# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    x, diff, answer = None, 0, 0
    
    for c in s:
        if x is None:
            x = c

        if x == c:
            diff += 1
        else:
            diff -= 1

        if diff == 0:
            answer += 1
            x = None
            diff = 0

    if diff != 0:
        answer += 1
        
    return answer
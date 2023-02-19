# https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer = 0
    
    for n in range(left, right+1):
        sqrt = n ** 0.5
        if int(sqrt) == sqrt:
            answer -= n
        else:
            answer += n
        
    return answer

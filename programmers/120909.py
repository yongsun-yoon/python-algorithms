# https://school.programmers.co.kr/learn/courses/30/lessons/120909

def solution(n):
    sqrt = n ** 0.5
    answer = 1 if sqrt == int(sqrt) else 2
    return answer

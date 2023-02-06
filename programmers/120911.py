# https://school.programmers.co.kr/learn/courses/30/lessons/120911

def solution(my_string):
    answer = ''.join(sorted([s.lower() for s in my_string]))
    return answer

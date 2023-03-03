# https://school.programmers.co.kr/learn/courses/30/lessons/120893

def solution(my_string):
    answer = ''.join([s.lower() if s.isupper() else s.upper() for s in my_string])
    return answer

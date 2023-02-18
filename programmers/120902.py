# https://school.programmers.co.kr/learn/courses/30/lessons/120902

def solution(my_string):
    answer = 0
    op = 1
    for i,s in enumerate(my_string.split(' ')):
        if i % 2 == 0:
            answer += int(s) * op
        else:
            op = 1 if s == '+' else -1
    return answer

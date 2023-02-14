# https://school.programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    answer = sum(set(range(10)) - set(numbers))
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/120912

def solution(array):
    string = ''.join(map(str, array))
    answer = string.count('7')
    return answer

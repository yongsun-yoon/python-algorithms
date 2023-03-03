# https://school.programmers.co.kr/learn/courses/30/lessons/120892

def solution(cipher, code):
    answer = ''.join([cipher[i-1] for i in range(code, len(cipher)+1, code)])
    return answer

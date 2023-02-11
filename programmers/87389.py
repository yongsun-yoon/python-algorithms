# https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    x = 2
    while True:
        if n % x == 1:
            break
        x += 1
        
    answer = x
    return answer

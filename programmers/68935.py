# https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    ternary = []
    d = 0
    while n > 0:
        n, r = divmod(n, 3)
        ternary.append(r)
    
    answer = 0
    for i, r in enumerate(ternary):
        answer += r * 3 ** (len(ternary)-i-1)
    return answer

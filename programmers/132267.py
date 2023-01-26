# https://school.programmers.co.kr/learn/courses/30/lessons/132267

def solution(a, b, n):
    answer = 0
    while n >= a:
        m, n = divmod(n, a)
        new = m * b
        n += new
        answer += new 
    return answer

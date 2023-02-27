# https://school.programmers.co.kr/learn/courses/30/lessons/120897

def solution(n):
    left, right = [], []
    for i in range(1, int(n**0.5)+1):
        s, r = divmod(n, i)
        if r == 0:
            left.append(i)
            if i != s:
                right.append(s)
                
    answer = left + right[::-1]
    return answer

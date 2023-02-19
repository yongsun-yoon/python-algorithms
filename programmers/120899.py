# https://school.programmers.co.kr/learn/courses/30/lessons/120899

def solution(array):
    max_idx, max_val = 0, 0
    for i, a in enumerate(array):
        if a > max_val:
            max_idx = i
            max_val = a
    answer = [max_val, max_idx]
    return answer

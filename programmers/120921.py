# https://school.programmers.co.kr/learn/courses/30/lessons/120921

def solution(A, B):
    answer = 0
    while answer < len(A):
        if A == B:
            return answer
        A = A[-1] + A[:-1]
        answer += 1
        
    return -1

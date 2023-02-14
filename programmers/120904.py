# https://school.programmers.co.kr/learn/courses/30/lessons/120904

def solution(num, k):
    answer = -1
    for i, n in enumerate(str(num)):
        if int(n) == k:
            answer = i + 1
            break
            
    return answer

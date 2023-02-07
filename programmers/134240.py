# https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    left, right = '', ''
    for i, f in enumerate(food):
        n = f // 2
        fs = str(i) * n
        left += fs
        right = fs + right
    
    answer = left + '0' + right
    return answer

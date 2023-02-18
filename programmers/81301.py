# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    words = [
        'zero', 'one', 'two', 'three', 'four', 
        'five', 'six', 'seven', 'eight', 'nine'
    ]
    
    for i, w in enumerate(words):
        s = s.replace(w, str(i))
    answer = int(s)
    return answer

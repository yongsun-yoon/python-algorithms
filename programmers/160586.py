# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    key2num = {}
    for key in keymap:
        for i, k in enumerate(key):
            n = key2num.get(k)
            if n is None or i+1 < n:
                key2num[k] = i+1
    
    
    answer = []
    for target in targets:
        num = 0
        for k in target:
            n = key2num.get(k)
            if n is None:
                num = -1
                break
            num += n
        
        answer.append(num)

    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/120896

def solution(s):
    cnt = {}
    for _s in s:
        _c = cnt.get(_s, 0)
        cnt[_s] = _c + 1
    
    answer = sorted([k for k,v in cnt.items() if v == 1])
    answer = ''.join(answer)
    return answer

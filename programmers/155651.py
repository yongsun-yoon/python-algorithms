# https://school.programmers.co.kr/learn/courses/30/lessons/155651

def time2min(t):
    h, m = t.split(':')
    m = int(h) * 60 + int(m)
    return m


def solution(book_time):
    time_table = [0] * (24*60)
    
    for s, e in book_time:
        s = time2min(s)
        e = time2min(e) + 10
        s = min(s, 24*60-1)
        e = min(e, 24*60-1)
        
        time_table[s] += 1
        time_table[e] -= 1
    
    answer = 0
    r = 0
    for t in time_table:
        r += t
        answer = max(answer, r)
        
    return answer

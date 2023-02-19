# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    min_cnt = len(set(lottos) & set(win_nums))
    max_cnt = min_cnt + lottos.count(0)
    min_rank = min(7 - min_cnt, 6)
    max_rank = min(7 - max_cnt, 6)
    answer = [max_rank, min_rank]
    return answer

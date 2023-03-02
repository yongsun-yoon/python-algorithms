# https://school.programmers.co.kr/learn/courses/30/lessons/42889

from collections import defaultdict


def solution(N, stages):
    stages = sorted(stages)
    
    n_total = defaultdict(int)
    n_fail = defaultdict(int)
    
    while stages:
        s = stages.pop(0)
        n_fail[s] += 1
        n_total[s] = max(len(stages)+1, n_total[s])

    rate = {i:n_fail.get(i, 0) / n_total.get(i, 1) for i in range(1, N+1)}
    answer = sorted(rate, key=lambda x: rate[x], reverse=True)
    return answer

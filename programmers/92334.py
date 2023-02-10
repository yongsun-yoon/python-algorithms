# https://school.programmers.co.kr/learn/courses/30/lessons/92334

from collections import defaultdict

def solution(id_list, report, k):
    id2idx = {i:idx for idx, i in enumerate(id_list)}
    accused_result = defaultdict(set)
        
    for r in report:
        user, accused = r.split()
        accused_result[accused].add(user)
    
    answer = [0] * len(id_list)
    for accused, users in accused_result.items():
        if len(users) >= k:
            for u in users:
                answer[id2idx[u]] += 1
        
    return answer

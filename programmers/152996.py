# https://school.programmers.co.kr/learn/courses/30/lessons/152996

from collections import defaultdict

def solution(weights):
    people = defaultdict(int)
    
    answer = 0
    for w in weights:
        answer += people[w] + people[w*2] + people[w/2] + people[w/2*3] + people[w/3*2] + people[w/3*4] + people[w/4*3]
        people[w] += 1
        
    return answer

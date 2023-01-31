# https://school.programmers.co.kr/learn/courses/30/lessons/118666

from collections import defaultdict

def solution(survey, choices):
    scores = defaultdict(int)
    for s, c in zip(survey, choices):
        if c < 4:
            scores[s[0]] += 4 - c
        elif c == 4:
            pass
        else:
            scores[s[1]] += c - 4
    
    answer = ''
    answer += 'R' if scores['R'] >= scores['T'] else 'T'
    answer += 'C' if scores['C'] >= scores['F'] else 'F'
    answer += 'J' if scores['J'] >= scores['M'] else 'M'
    answer += 'A' if scores['A'] >= scores['N'] else 'N'
    return answer

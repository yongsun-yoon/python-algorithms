# https://school.programmers.co.kr/learn/courses/30/lessons/133499

phonemes = ['aya', 'ye', 'woo', 'ma']

def solution(babbling):
    answer = 0
    
    for b in babbling:
        for p in phonemes:
            if p * 2 not in b:
                b = b.replace(p, ' ')
        
        if len(b.strip()) == 0:
            answer += 1
                
    return answer

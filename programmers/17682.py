# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    bonuses = ['S', 'D', 'T']
    answer = 0
    
    pp, p = 0, 0
    i = 0
    while i < len(dartResult):
        r = dartResult[i]
        
        if r.isdigit():
            if dartResult[i+1].isdigit():
                r = dartResult[i:i+2]
                i += 1
            pp = p
            p = int(r)
            
        elif r in bonuses:
            p = p ** (bonuses.index(r) + 1)
            answer += p
        
        else:
            if r  == '*':
                answer += pp + p
                p *= 2
                pp *= 2
                
            else:
                answer -= p * 2
                p *= -1
        
        i += 1
        
    return answer

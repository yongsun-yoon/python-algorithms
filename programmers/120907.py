# https://school.programmers.co.kr/learn/courses/30/lessons/120907

def solution(quiz):
    answer = []
    
    for q in quiz:
        x, o, y, _, z = q.split()
        x, y, z = int(x), int(y), int(z)
        
        _z = x + y if o == '+' else x - y
        
        if z == _z:
            answer.append('O')
        else:
            answer.append('X')
            
    return answer

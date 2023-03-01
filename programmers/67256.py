# https://school.programmers.co.kr/learn/courses/30/lessons/67256

keys = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
key2pos = {keys[i][j]: [i,j] for j in range(3) for i in range(4)}

def dist_fn(p1, p2):
    return sum([abs(_p1-_p2) for _p1, _p2 in zip(p1, p2)])

def solution(numbers, hand):
    answer = ''
    left, right = '*', '#'
    
    for n in numbers:
        if n in [1, 4, 7]:
            nxt = 'left'
            
        elif n in [3, 6, 9]:
            nxt = 'right'
            
        else:
            left_dist = dist_fn(key2pos[left], key2pos[n])
            right_dist = dist_fn(key2pos[right], key2pos[n])
            if left_dist < right_dist:
                nxt = 'left'
            elif left_dist > right_dist:
                nxt = 'right'
            else:
                nxt = hand
            
        if nxt == 'left':
            answer += 'L'
            left = n
        else:
            answer += 'R'
            right = n
            
    return answer

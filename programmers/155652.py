# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    alphabet = list(map(chr, range(97, 123)))
    alphabet = [a for a in alphabet if a not in skip]
    
    answer = ''
    for _s in s:
        new_index = alphabet.index(_s) + index
        while new_index >= len(alphabet):
            new_index -= len(alphabet)
        answer += alphabet[new_index]
    
    return answer

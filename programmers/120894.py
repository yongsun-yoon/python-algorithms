# https://school.programmers.co.kr/learn/courses/30/lessons/120894

def solution(numbers):
    number_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    number_words = {w:str(i) for i,w in enumerate(number_words)}
    
    answer = ''
    buffer = ''
    for e in numbers:
        buffer += e
        n = number_words.get(buffer)
        if n is not None:
            answer += n
            buffer = ''
    answer = int(answer)
    return answer

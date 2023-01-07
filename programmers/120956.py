# https://school.programmers.co.kr/learn/courses/30/lessons/120956


def check_available(word, vocab):
    while word:
        removed = False
        for v in vocab:
            if word.startswith(v):
                word = word[len(v):]
                removed = True
        
        if not removed:
            break
    
    is_available = True if len(word) == 0 else False
    return is_available


def solution(babbling):
    vocab = ["aya", "ye", "woo", "ma"]
    answer = sum([check_available(word, vocab) for word in babbling])
    return answer
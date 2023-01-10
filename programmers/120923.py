# https://school.programmers.co.kr/learn/courses/30/lessons/120923


def solution(num, total):
    a, b = divmod(total, num)
    
    if b == 0:
        i = a - num // 2

    else:
        i = a - (num // 2 - 1)

    answer = list(range(i, i+num))

    return answer
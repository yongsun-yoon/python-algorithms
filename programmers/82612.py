# https://school.programmers.co.kr/learn/courses/30/lessons/82612


def solution(price, money, count):
    total_price = price * count * (count+1) / 2
    answer = max(total_price - money, 0)
    return answer

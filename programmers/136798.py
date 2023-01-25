# https://school.programmers.co.kr/learn/courses/30/lessons/136798

def solution(number, limit, power):
    powers = [0] * number
    for i in range(1, number+1):
        j = 1
        while j * i <= number:
            powers[j*i-1] += 1
            j += 1
    
    powers = [p if p <= limit else power for p in powers]
    answer = sum(powers)
    return answer

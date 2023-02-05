# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    num_classes = len(set(nums))
    max_cnt = len(nums) // 2
    answer = min(num_classes, max_cnt)
    return answer

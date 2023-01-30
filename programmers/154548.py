# https://school.programmers.co.kr/learn/courses/30/lessons/154538

from collections import deque

def solution(x, y, n):
    stack = deque([[y, 0]])
    while stack:
        y, cnt = stack.popleft()
        
        if y == x:
            return cnt
        if y < x:
            continue

        if y % 2 == 0:
            stack.append([y/2, cnt+1])
        if y % 3 == 0:
            stack.append([y/3, cnt+1])
        
        stack.append([y-n, cnt+1])

    return -1

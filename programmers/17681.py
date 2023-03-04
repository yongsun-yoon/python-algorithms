# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    
    for row1, row2 in zip(arr1, arr2):
        row = bin(row1 | row2)
        row = row[2:].zfill(n)
        row = row.replace('1', '#').replace('0', ' ')
        answer.append(row)
    
    return answer

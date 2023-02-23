# https://school.programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    new_id = re.sub('[.]{2,}', '.', new_id)
    new_id = new_id[1:] if new_id.startswith('.') else new_id
    new_id = new_id[:-1] if new_id.endswith('.') else new_id
    new_id = 'a' if not new_id else new_id
    new_id = new_id[:15]
    new_id = new_id[:-1] if new_id.endswith('.') else new_id
    while len(new_id) < 3:
        new_id = new_id + new_id[-1]
    return new_id

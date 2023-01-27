# https://school.programmers.co.kr/learn/courses/30/lessons/154540

from collections import deque


def solution(maps):    
    N, M = len(maps), len(maps[0])
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    answer = []
    for i in range(N):
        for j in range(M):
            if maps[i][j]=='X' or visited[i][j]:
                continue
                
            queue = deque()
            queue.append((i,j))
            food = int(maps[i][j])
            visited[i][j] = True
            
            while queue:
                qi, qj = queue.popleft()
                for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                    ni = qi + di
                    nj = qj + dj
                    
                    if ni < 0 or ni >= N or nj < 0 or nj >= M:
                        continue
                    if visited[ni][nj] or maps[ni][nj] == 'X':
                        continue
                    
                    queue.append((ni,nj))
                    visited[ni][nj] = True
                    food += int(maps[ni][nj])
                    
            answer.append(food)
    
    if not answer:
        answer.append(-1)
    
    answer.sort()
    return answer

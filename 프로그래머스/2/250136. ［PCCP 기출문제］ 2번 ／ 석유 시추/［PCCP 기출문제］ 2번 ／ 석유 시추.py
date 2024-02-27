from collections import deque
def solution(land):
    n = len(land)
    m = len(land[0])
    
    columns_total = [0] * m
   	
    visit = [[False] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 0 or visit[i][j]: continue
            
            visit[i][j] = True
            queue = deque([(i, j)])
            
            columns = set([j])
            count = 1
            while queue:
                ci, cj = queue.pop()
                
                for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                    ni, nj = ci + dx, cj + dy
                    
                    if not (0 <= ni < n) or not (0 <= nj < m): continue
                    if land[ni][nj] == 0 or visit[ni][nj]: continue
                   	
                    columns.add(nj)
                    queue.append((ni, nj))
                    visit[ni][nj] = True
                    count += 1
            
            for c in columns:
                columns_total[c] += count
    
    answer = 0 
    for idx, c in enumerate(columns_total):
        if c > answer:
            answer = c
    return answer
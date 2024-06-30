from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = -1
    
    queue = deque([(0, 0, 1)])
    visit = [[False] * m for _ in range(n)]
    
    while queue:
        x, y, count = queue.popleft()
        
        if (x, y) == (n-1, m-1):
            answer = count
            break
        
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if not(0 <= nx < n and 0<= ny < m):
                continue
            if visit[nx][ny]: continue
            if maps[nx][ny] == 0: continue
            
            queue.append((nx, ny, count+1))
            visit[nx][ny] = True
    
    return answer
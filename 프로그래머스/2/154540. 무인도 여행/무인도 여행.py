def solution(maps):
    maps = list(map(list, maps))
    answer = []
   	
    n = len(maps)
    m = len(maps[0])
    v = [[False]*m for _ in range(n)]
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for i in range(n):
        for j in range(m):
            if v[i][j]: continue
            if maps[i][j] == 'X': continue
            
            day = int(maps[i][j])
            stack = [(i, j)]
            v[i][j] = True
            
            while stack:
                x, y = stack.pop()
                
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if not(0<= nx < n and 0<= ny < m): continue
                    if v[nx][ny]: continue
                    if maps[nx][ny] == 'X': continue
                    
                    day += int(maps[nx][ny])
                    v[nx][ny] = True
                    stack.append((nx, ny))
            answer.append(day)
    answer = sorted(answer)
    if not answer:
        return [-1]
    return answer
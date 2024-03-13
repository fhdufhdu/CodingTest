from collections import deque
def solution(maps):
    maps = list(map(lambda x:list(x), maps))
    n = len(maps)
    m = len(maps[0])
    
    s = None
    l = None
    e = None
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                s = (i, j)
                maps[i][j] = 'O'
            elif maps[i][j] == 'L':
                l = (i, j)
                maps[i][j] = 'O'
            elif maps[i][j] == 'E':
                e = (i, j)
                maps[i][j] = 'O'
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    queue = deque([(s[0], s[1], 0)])
    v = [[False] * m for _ in range(n)]
    v[s[0]][s[1]] = True
   	
    s_to_l = -1
    while queue:
        x, y, count = queue.popleft()
        if (x, y) == l:
            s_to_l = count
            break
        
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if not(0<=nx<n and 0<=ny<m): continue
            if maps[nx][ny] == 'X': continue
            if v[nx][ny]: continue
            
            queue.append((nx, ny, count+1))
            v[nx][ny] = True
            
    queue = deque([(l[0], l[1], 0)])
    v = [[False] * m for _ in range(n)]
    v[l[0]][l[1]] = True
   	
    l_to_e = -1
    while queue:
        x, y, count = queue.popleft()
        if (x, y) == e:
            l_to_e = count
            break
        
        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if not(0<=nx<n and 0<=ny<m): continue
            if maps[nx][ny] == 'X': continue
            if v[nx][ny]: continue
            
            queue.append((nx, ny, count+1))
            v[nx][ny] = True
    
    if s_to_l == -1 or l_to_e == -1:
        return -1
    answer = s_to_l + l_to_e
    return answer
from sys import stdin, stdout
from collections import deque
from typing import List

read = stdin.readline
write = stdout.write

result_list = []
count = [[[[0] * 20 for _ in range(20)] for _ in range(20)] for _ in range(20)]
while True:
    n, m = list(map(int, read().rsplit(' ')))
    n, m = m, n
    if n == 0 and m == 0:
        break
    
    data = [list(read().rstrip()) for _ in range(n)]
    v = [[-1] * m for _ in range(n)]

    robot = None
    dirty = []
    for i in range(n):
        for j in range(m):
            if data[i][j] == 'o':
                robot = (i, j)
            elif data[i][j] == '*':
                dirty.append((i, j))

    path:List[list] = [] 
    dfsv = [False] * len(dirty)
    
    for idx, r in enumerate(dirty + [robot]):
        rx, ry = r

        deq = deque([(rx, ry, 0)])
        v[rx][ry] = idx

        while deq:
            x, y, move = deq.popleft()

            if data[x][y] == '*' and (rx, ry) != (x, y):
                count[rx][ry][x][y] = move
                count[x][y][rx][ry] = move
                
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                nx, ny = x + dx, y + dy

                if not(0<=nx<n and 0<=ny<m): continue
                if v[nx][ny] == idx: continue
                if data[nx][ny] == 'x': continue

                v[nx][ny] = idx
                deq.append((nx, ny, move+1))

    mv = 1000000000000
    def dfs(depth:int, history:list):
        global dfsv, mv
        if depth == len(dirty):
            su = 0
            for i in range(depth):
                if count[history[i][0]][history[i][1]][history[i+1][0]][history[i+1][1]] == 0:
                    su = 0
                    break
                su += count[history[i][0]][history[i][1]][history[i+1][0]][history[i+1][1]]
            mv = min(mv, su)
            return
        
        for idx, d in enumerate(dirty):
            if dfsv[idx]: continue
            dfsv[idx] = True
            dfs(depth+1, history+[d])
            dfsv[idx] = False
    
    dfs(0, [robot]) 
    
    if mv == 0: mv = -1
    result_list.append(str(mv))

write("\n".join(result_list))
from sys import stdin, stdout
from collections import deque

read = stdin.readline
write = stdout.write

n, m = list(map(int, read().rsplit(' ')))
data = [list(map(int, read().rsplit(' '))) for _ in range(n)]
ans = [[(-1, 1000000000)] * n for _ in range(n)]
va = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 2:
            va.append((i, j))
        elif data[i][j] == 1:
            ans[i][j] = (-1, '-')

virus = []
o = [0] * m
v = [False] * len(va)
def dfs(depth:int):
    if depth == m:
        virus.append([o[i] for i in range(m)])
        return

    s = o[depth - 1]
    if depth - 1 < 0:
        s = 0
    for i in range(s, len(va)):
        if v[i]: continue
        v[i] = True
        o[depth] = i
        dfs(depth+1)
        v[i] = False

dfs(0)

min_v = 1000000000
for idx, vo in enumerate(virus):
    deq = deque()
    for o in vo:
        deq.append((*va[o], 0))
        ans[va[o][0]][va[o][1]] = (idx, 0)
    
    while deq:
        x, y, move = deq.popleft()

        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            nx, ny = x + dx, y + dy
            if not(0<=nx<n and 0<=ny<n): continue
            if data[nx][ny] == 1: continue
            if ans[nx][ny][0] == idx and ans[nx][ny][1] <= move + 1: continue

            ans[nx][ny] = (idx, move+1)
            deq.append((nx, ny, move+1))
    
    

    mv = 0
    is_reach = True
    for i in range(n):
        for j in range(n):
            if ans[i][j][1] == '-': continue
            if ans[i][j][0] != idx and data[i][j] != 1: 
                is_reach = False
                break
            mv = max(mv, ans[i][j][1])
        if not is_reach: break
    if is_reach:
        min_v = min(mv, min_v)

if min_v == 1000000000:
    min_v = -1
write(str(min_v))
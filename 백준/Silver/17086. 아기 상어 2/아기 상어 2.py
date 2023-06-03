from sys import stdin, stdout
from collections import deque

read = stdin.readline
write = stdout.write

n, m = list(map(int, read().rsplit(' ')))
data = [list(map(int, read().rsplit(' '))) for _ in range(n)]
ans = [[50**2+1] * m for _ in range(n)]
v = [[-1] * m for _ in range(n)]

shark = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            shark.append((i, j))

for idx, (i, j) in enumerate(shark):
    deq = deque([(i, j, 0)])
    ans[i][j] = 0
    v[i][j] = idx

    while deq:
        x, y, move = deq.popleft()

        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1):
            nx, ny = x + dx, y + dy

            if not(0<=nx<n and 0<=ny<m): continue
            if v[nx][ny] == idx: continue
            if data[nx][ny] == 1: continue
            
            v[nx][ny] = idx
            if ans[nx][ny] > move + 1:
                ans[nx][ny] = move + 1
            deq.append((nx, ny, move + 1))

result = max([max(ans[i]) for i in range(n)])
write(str(result))
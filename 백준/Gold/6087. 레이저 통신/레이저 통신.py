from sys import stdin, stdout
from collections import deque

read = stdin.readline
write = stdout.write

n, m = list(map(int, read().rsplit(' ')))
n, m = m, n
data = [list(read().rstrip()) for _ in range(n)]
w = [[[-1]*4 for _ in range(m)] for _ in range(n)]

start = None
for i in range(n):
    for j in range(m):
        if data[i][j] == 'C':
            start = (i, j)
            data[i][j] = '.'
            w[i][j][0] = 0
            w[i][j][1] = 0
            w[i][j][2] = 0
            w[i][j][3] = 0
            break
    if start is not None: break

deq = deque([(*start, -1, -1)])

minv = 987654321
while deq:
    x, y, d, w_= deq.popleft()

    if data[x][y] == 'C':
        minv = min(minv, w_)

    for idx, (dx, dy) in enumerate(((1, 0), (-1, 0), (0, 1), (0, -1))):
        nx, ny = x + dx, y + dy
        if not(0<=nx<n and 0<=ny<m): continue
        if data[nx][ny] == '*': continue
        if 0<= w[nx][ny][idx] <= w_: continue

        if idx == d:
            w[nx][ny][idx] = w_
            deq.append((nx, ny, idx, w_))
        else:
            w[nx][ny][idx] = w_+1
            deq.append((nx, ny, idx, w_+1))

write(str(minv))
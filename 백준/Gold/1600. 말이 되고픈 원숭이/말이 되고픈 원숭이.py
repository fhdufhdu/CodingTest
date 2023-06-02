from collections import deque
from sys import stdin, stdout

read = stdin.readline
write = stdout.write

kk = int(read().rstrip())
w, h = list(map(int, read().rsplit(' ')))
data = [list(map(int, read().rsplit(' '))) for _ in range(h)]
v = [[[False] * w for _ in range(h)] for _ in range(kk+1)]

if data[0][0] == 1 or data[h-1][w-1] == 1:
    write('-1')
    exit()
deq = deque([(0, 0, 0, 0)])
v[kk][0][0] = True

while deq:
    x, y, m, k = deq.popleft()

    if x == h-1 and y == w-1:
        write(str(m))
        exit()

    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
        nx, ny = x + dx, y + dy
        if not(0<=nx<h and 0<=ny<w): continue
        if v[k][nx][ny]: continue
        if data[nx][ny] == 1: continue

        v[k][nx][ny] = True
        deq.append((nx, ny, m+1, k))

    if k < kk:
        for dx, dy in (-1, -2), (-2, -1), (-1, 2), (-2, 1), (1, -2), (2, -1), (1, 2), (2, 1):
            nx, ny = x + dx, y + dy
            if not(0<=nx<h and 0<=ny<w): continue
            if v[k+1][nx][ny]: continue
            if data[nx][ny] == 1: continue

            v[k+1][nx][ny] = True
            deq.append((nx, ny, m+1, k+1))

write('-1')
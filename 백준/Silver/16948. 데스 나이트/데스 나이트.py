from sys import stdin, stdout

read = stdin.readline
write = stdout.write


n = int(read().rstrip())
r1, c1, r2, c2 = list(map(int, read().rsplit(' ')))
v = [[False] * n for _ in range(n)]

d = ((-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1))

from collections import deque

deq = deque([(r1, c1, 0)])
v[r1][c1] = True

while deq:
    x, y, cnt = deq.popleft()

    if x == r2 and y == c2:
        write(str(cnt))
        exit()

    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if not(0<=nx<n and 0<=ny<n): continue
        if v[nx][ny]: continue

        v[nx][ny] = True
        deq.append((nx, ny, cnt+1))

write('-1')

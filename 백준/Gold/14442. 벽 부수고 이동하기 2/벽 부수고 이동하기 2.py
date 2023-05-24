from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n, m, k = list(map(int, read().rsplit(" ")))
data = [list(map(int, read().rstrip())) for _ in range(n)]

v = [[[False] * (k+1) for _ in range(m)] for _ in range(n)]

from collections import deque

deq = deque([(0, 0, 1, 0)])
v[0][0][0] = True

while deq:
    i, j, move_cnt, break_cnt = deq.popleft()
    if i == n-1 and j == m-1:
        write(str(move_cnt))
        exit()

    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx = i + dx
        ny = j + dy
        if not(0<=nx<n and 0<=ny<m): continue

        if data[nx][ny] == 0:
            if v[nx][ny][break_cnt]: continue
            v[nx][ny][break_cnt] = True
            deq.append((nx, ny, move_cnt+1, break_cnt))
        else:
            if break_cnt >= k: continue
            if v[nx][ny][break_cnt+1]: continue
            v[nx][ny][break_cnt + 1] = True
            deq.append((nx, ny, move_cnt+1, break_cnt + 1))

write('-1')
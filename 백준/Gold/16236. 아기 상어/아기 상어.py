from collections import deque
from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n = int(read().rstrip())
data = [list(map(int, read().rsplit(' '))) for _ in range(n)]

shark = None
for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            shark = (i, j)
            break

sx, sy = shark
data[sx][sy] = 0
v = [[-1] * n for _ in range(n)]
sdeq = deque([(sx, sy, 2, 0)])

total_eat_cnt = 0
result = 0

while sdeq:
    ssx, ssy, ssize, eat_cnt = sdeq.popleft()

    deq = deque([(ssx, ssy, ssize, 0)])
    v[ssx][ssy] = total_eat_cnt

    eat_able = []
    while deq:
        x, y, size, move_cnt = deq.popleft()

        for dx, dy in (-1, 0), (0, -1), (0, 1), (1, 0):
            nx = x + dx
            ny = y + dy
            if not(0<=nx<n and 0<=ny<n): continue
            if v[nx][ny] == total_eat_cnt: continue
            if data[nx][ny] > size: continue

            if data[nx][ny] == size or data[nx][ny] == 0:
                v[nx][ny] = total_eat_cnt
                deq.append((nx, ny, size, move_cnt+1))
            else:
                v[nx][ny] = total_eat_cnt
                eat_able.append((move_cnt+1, nx, ny))

    if not eat_able: break

    eat_able = sorted(eat_able, key=lambda x:(x[0], x[1], x[2]))
    move_cnt, ex, ey = eat_able[0]    

    result += move_cnt
    data[ex][ey] = 0
    total_eat_cnt += 1
    eat_cnt += 1

    if ssize == eat_cnt:
        ssize += 1
        eat_cnt = 0
    
    sdeq.append((ex, ey, ssize, eat_cnt))

write(str(result))

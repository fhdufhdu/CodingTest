from collections import deque
from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n, m, k = list(map(int, read().rsplit(' ')))
data = [list(map(int, list(read().rstrip()))) for _ in range(n)]

v = [[False] * 1000 for _ in range(1000)]
b = [[0] * 1000 for _ in range(1000)]
# 0이 낮, 1이 밤
deq = deque([(0, 0, 1, 0, 0)])
v[0][0] = True

while deq:
    x, y, move_cnt, break_cnt, is_night = deq.popleft()

    if x == n-1 and y == m-1:
        write(str(move_cnt))
        exit()

    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx = x + dx
        ny = y + dy
        if not(0<=nx<n and 0<=ny<m): continue

        if data[nx][ny] == 0:
            if v[nx][ny] and b[nx][ny] <= break_cnt: continue
            v[nx][ny] = True
            b[nx][ny] = break_cnt
            deq.append((nx, ny, move_cnt+1, break_cnt, int(not is_night)))
        else:
            if break_cnt >= k: continue
            if is_night:
                deq.append((x, y, move_cnt+1, break_cnt, int(not is_night)))
            else:
                if v[nx][ny] and b[nx][ny] <= break_cnt+1: continue
                v[nx][ny] = True
                b[nx][ny] = break_cnt + 1
                deq.append((nx, ny, move_cnt+1, break_cnt+1, int(not is_night)))

write('-1')
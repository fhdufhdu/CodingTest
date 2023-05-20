from collections import deque
from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n = int(read().rstrip())
data = [list(read().rstrip()) for _ in range(n)]
color = [[0]*n for _ in range(n)]
v = [[False]*n for _ in range(n)]
direction = ((0, -1), (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0))

max_cnt = 0
for i in range(n):
    for j in range(n):
        if data[i][j] == '-': continue
        if v[i][j]: continue

        stack = [(i, j)]
        v[i][j] = True
        while stack:
            x, y = stack.pop()
            color_set = set()
            for dx, dy in direction:
                ii = x + dx
                jj = y + dy
                if not(0 <= ii < n and 0 <= jj < n): continue
                color_set.add(color[ii][jj])

            for k in range(1, 2600):
                if k not in color_set:
                    color[x][y] = k
                    max_cnt = max(max_cnt, k)
                    break
             
            for dx, dy in direction:
                ii = x + dx
                jj = y + dy
                if not(0 <= ii < n and 0 <= jj < n): continue
                if v[ii][jj]: continue
                if data[ii][jj] == '-': continue
                v[ii][jj] = True
                stack.append((ii, jj))

if max_cnt > 3:
    max_cnt = 3
write(str(max_cnt))

from sys import stdin, stdout
from collections import deque

read = stdin.readline
write = stdout.write

n, m = list(map(int, read().rsplit(' ')))
data = [list(read().rstrip()) for _ in range(m)]
visit = [[False] * n for _ in range(m)]

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

b = 0
w = 0
for i in range(m):
    for j in range(n):
        if visit[i][j]: continue

        cnt = 0
        stack = [(i, j)]
        visit[i][j] = True
        while(stack):
            cnt += 1
            x, y = stack.pop()
            for dx, dy in d:
                x_ = x + dx
                y_ = y + dy
                if not (0 <= x_ < m and 0 <= y_ < n): continue
                if visit[x_][y_]: continue
                if data[x][y] != data[x_][y_]: continue
                stack.append((x_, y_))
                visit[x_][y_] = True

        if data[i][j] == 'W':
            w += cnt ** 2
        else:
            b += cnt ** 2

write(f'{w} {b}')
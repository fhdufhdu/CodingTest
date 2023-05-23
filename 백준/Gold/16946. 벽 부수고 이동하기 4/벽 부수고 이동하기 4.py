from collections import deque
from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n, m = list(map(int, read().rsplit(' ')))
data = [list(read().rstrip()) for _ in range(n)]

zero = [["-1/-1"] * m for _ in range(n)]
v = [[-1] * m for _ in range(n)]

result = [['0'] * m for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        current_idx = i * n + j

        if data[i][j] == '1': continue
        if zero[i][j] != '-1/-1': continue

        stack = [(i, j)]
        v[i][j] = current_idx

        history = []
        while stack:
            x, y = stack.pop()
            history.append((x, y))
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                nx, ny = x + dx, y + dy
                if not(0<=nx<n and 0<=ny<m): continue
                if v[nx][ny] == current_idx: continue
                if data[nx][ny] == '1': continue

                v[nx][ny] = current_idx
                stack.append((nx, ny))

        hlen = len(history)        
        for x, y in history:
            zero[x][y] = f"{cnt}/{hlen}"
        cnt += 1

for i in range(n):
    for j in range(m):
        if data[i][j] == '0': continue

        set_ = set()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = i + dx, j + dy
            if not(0<=nx<n and 0<=ny<m): continue
            if data[nx][ny] == '1': continue
            set_.add(zero[nx][ny])
        zero_list = list(map(lambda x:int(x.split('/')[1]), list(set_)))
        result[i][j] = str((sum(zero_list) + 1) % 10)

result = ["".join(d) for d in result]
write("\n".join(result))
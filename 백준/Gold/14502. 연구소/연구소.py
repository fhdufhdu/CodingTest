from collections import deque
from sys import stdin, stdout

read = stdin.readline
write = stdout.write


n, m = list(map(int, read().rsplit(' ')))
data = [list(map(int, read().rsplit( ))) for _ in range(n)]
N = n * m
visit = [[-1] * m for _ in range(n)]

w = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            a1, b1 = i // m, i % m
            a2, b2 = j // m, j % m
            a3, b3 = k // m, k % m
            if not(data[a1][b1] == 0 and data[a2][b2] == 0 and data[a3][b3] == 0):
                continue
            w.append(((a1, b1), (a2, b2), (a3, b3)))

direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
maxv = -1
for idx, w_ in enumerate(w): 
    for a, b in w_:
        data[a][b] = 1

    for i in range(n):
        for j in range(m):        
            if data[i][j] != 2: continue
            if visit[i][j] == idx: continue

            deq = deque([(i, j)])
            visit[i][j] = idx

            while deq:
                x, y = deq.popleft()

                for dx, dy in direction:
                    nx = x + dx
                    ny = y + dy
                    if not(0<= nx <n and 0<=ny<m): continue
                    if data[nx][ny] != 0: continue
                    if visit[nx][ny] == idx: continue

                    visit[nx][ny] = idx
                    deq.append((nx, ny))
    sumv = 0 
    for i in range(n):
        for j in range(m):
            if visit[i][j] != idx and data[i][j] == 0:
                sumv += 1
    maxv = max(maxv, sumv)

    for a, b in w_:
        data[a][b] = 0

write(str(maxv))
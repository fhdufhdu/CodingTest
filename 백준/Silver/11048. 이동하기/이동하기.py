from sys import stdin, stdout
from collections import deque

read = stdin.readline
write = stdout.write

n, m = list(map(int, read().rsplit(' ')))
data = [list(map(int, read().rsplit(' '))) for _ in range(n)]
ans = [[0] * m for _ in range(n)]
ans[0][0] = data[0][0]

for i in range(n):
    for j in range(m):
        for di, dj in (1, 0), (0, 1), (1, 1):
            ni, nj = i + di, j + dj
            if not(0<=ni<n and 0<=nj<m): continue

            s = ans[i][j] + data[ni][nj]
            if ans[ni][nj] < s:
                ans[ni][nj] = s
        
write(str(ans[n-1][m-1]))
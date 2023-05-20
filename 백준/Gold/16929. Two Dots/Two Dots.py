from collections import deque
from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n, m = list(map(int, read().rsplit(' ')))
data = [list(read().rstrip()) for _ in range(n)]
visit = [[False] * m for _ in range(n)] 
direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

result = False
def dfs(i:int, j:int, dhistory:set):
    global result
 
    for idx, (dx, dy) in enumerate(direction):
        ii = i + dx     
        jj = j + dy
        if not (0<= ii < n and 0 <= jj < m): continue
        if data[i][j] != data[ii][jj]: continue
        if visit[ii][jj] and \
            ((len(dhistory) == 3 and idx not in dhistory) or \
            (len(dhistory) == 4)):
            result = True
            return
        if visit[ii][jj]: continue

        visit[ii][jj] = True
        dhistory.add(idx)
        dfs(ii, jj, dhistory)

for i in range(n):
    for j in range(m):
        visit[i][j] = True
        dfs(i, j, set([]))

result_str = "Yes" if result else "No"
write(result_str)

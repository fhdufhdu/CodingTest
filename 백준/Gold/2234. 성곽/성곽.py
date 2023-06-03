from sys import stdin, stdout
from collections import deque

read = stdin.readline
write = stdout.write

n, m = list(map(int, read().rsplit(' ')))
n, m = m, n

data = [list(map(int, read().rsplit(' '))) for _ in range(n)]

def to_binary(num:int):
    result = []
    while num > 0:
        result.append(num % 2)
        num = num // 2
    while len(result) != 4:
        result.append(0)
    result.reverse()
    return result

for i in range(n):
    for j in range(m):
        data[i][j] = to_binary(data[i][j])

v = [[False] * m for _ in range(n)]
ans3 = [[1] * m for _ in range(n)]

ans1 = 0
ans2 = 0
ans3_ = 0
for i in range(n):
    for j in range(m):
        if v[i][j]: continue
        
        mh = [(i, j)]
        deq = deque([(i, j)])
        v[i][j] = True

        while deq:
            x, y= deq.popleft()

            for idx, (dx, dy) in enumerate([(1, 0), (0, 1), (-1, 0), (0, -1)]):
                if data[x][y][idx] == 1: continue
                nx, ny = x + dx, y + dy

                if not(0<=nx<n and 0<=ny<m): continue
                if v[nx][ny]: continue

                v[nx][ny] = True
                mh.append((nx, ny))
                deq.append((nx, ny))

        ans1 += 1
        ans2 = max(ans2, len(mh))
        for x, y in mh:
            ans3[x][y] = (ans1, len(mh))
            
for i in range(n):
    for j in range(m):
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx, ny = i + dx, j + dy
            if not(0<=nx<n and 0<=ny<m): continue
            if ans3[i][j][0] == ans3[nx][ny][0]: continue
            ans3_ = max(ans3_, ans3[i][j][1] + ans3[nx][ny][1])

write(f"{ans1}\n{ans2}\n{ans3_}")
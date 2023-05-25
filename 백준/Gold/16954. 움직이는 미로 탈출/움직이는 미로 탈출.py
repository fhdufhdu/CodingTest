from collections import deque
from sys import stdin, stdout

read = stdin.readline
write = stdout.write

data = [list(read().rstrip()) for _ in range(8)]
data1 = data.copy()
v = [[False] * 8 for _ in range(8)]

deq = deque([(7, 0, 0)])
v[7][0] = True

while deq:
    x, y, cnt = deq.popleft()

    if x == 0 and y == 7:
        write("1")
        exit()

    data1 = deque(data.copy())
    for i in range(cnt):
        data1.appendleft([".", ".", ".", ".",".", ".", ".", "."])
        data1.pop() 

    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0):
        nx = x + dx
        ny = y + dy
        if not(0<=nx<8 and 0<=ny<8): continue
        if v[nx][ny] and not (x == nx and y == ny):continue
        if data1[nx][ny] == '#': continue

        data1.appendleft([".", ".", ".", ".",".", ".", ".", "."])
        origin = data1.pop()
        if data1[nx][ny] == "#": 
            data1.append(origin)
            data1.popleft()
            continue

        v[nx][ny] = True
        deq.append((nx, ny, cnt+1))

        data1.append(origin)
        data1.popleft()

write("0")

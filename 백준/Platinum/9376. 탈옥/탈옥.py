from collections import deque
from sys import stdin, stdout

read = stdin.readline
write = stdout.write

t = int(read().rstrip())

result = []
for _ in range(t):
    h, w = list(map(int, read().rsplit(' ')))
    h, w = h+2, w+2
    data = []
    for i in range(h):
        if i == 0 or i == h-1:
            data.append("." * w)
        else:
            data.append(["."] + list(read().rstrip()) + ["."])
    v = [[[100000000] * w for _ in range(h)] for _ in range(3)]

    start_list = [(0, 0)]
    for i in range(h):
        for j in range(w):
            if data[i][j] == '$':
                start_list.append((i, j))

    cnt = 0
    for idx, (si, sj) in enumerate(start_list):
        deq = deque([(si, sj, [])])
        v[idx][si][sj] = 0

        while deq:
            x, y, history = deq.popleft()
            b = len(history)
 
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                nx, ny = x + dx, y + dy
                if not(0<= nx <h and 0<= ny < w): continue
                if data[nx][ny] == '*': continue

                weight = 1 if data[nx][ny] == '#' else 0

                if v[idx][nx][ny] > b + weight:
                    v[idx][nx][ny] = b + weight
                    if weight == 1:
                        deq.append((nx, ny, history + [(nx, ny)]))
                    else:
                        deq.appendleft((nx, ny, history))

    mv = 1000000000    
    for i in range(h):
        for j in range(w):
            su = sum([v[0][i][j],v[1][i][j],v[2][i][j]])
            if data[i][j] == '#':
                su -= 2
            mv = min(su, mv)
    
    result.append(str(mv))
write("\n".join(result))
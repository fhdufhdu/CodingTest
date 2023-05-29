from sys import stdin, stdout
from collections import deque

read = stdin.readline
write = stdout.write

f, s, g, u, d = list(map(int, read().rsplit(' ')))
d = -d
v = [False] * 1000001

deq = deque([(s, 0)])
v[s] = True

while deq:
    num, cnt = deq.popleft()

    if num == g:
        write(str(cnt))
        exit()
    
    for b in u, d:
        next_num = num + b
        if not(1<= next_num <= f): continue
        if v[next_num]: continue

        v[next_num] = True
        deq.append((next_num, cnt+1))

write('use the stairs')
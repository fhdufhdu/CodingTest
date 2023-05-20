from collections import deque
from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n = int(read().rstrip())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = list(map(int, read().rsplit(' ')))
    g[a].append(b)
    g[b].append(a)
o = deque(list(map(int, read().rsplit(' '))))
o.popleft()

v = [False] * (n+1)
deq = deque([1])

v[1] = True

while deq:
    node = deq.popleft()
    history = []
         
    for next in g[node]:
        if v[next]: continue
        v[next] = True
        history.append(next)
    history = sorted(history)
    oo = sorted([o[i] for i in range(len(history))])
    if history != oo:
        write('0')
        exit()
    for i in range(len(history)):
        deq.append(o.popleft())

write('1')
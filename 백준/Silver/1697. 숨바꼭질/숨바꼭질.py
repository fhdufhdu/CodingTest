from sys import stdin, stdout
from collections import deque 

read = stdin.readline
write = stdout.write

a, b = list(map(int, read().rstrip().split(' ')))

g = [[] for _ in range(100001)]
v = [False] * 100001

for i in range(100001):
    w = i + 1
    t = i * 2
    if w < 100001:
        g[i].append(w)
        g[w].append(i)
    if t < 100001:
        g[i].append(t)

result = []
deq = deque([(a, 0)])
v[a] = True
while deq:
    node_, cnt = deq.popleft()
    if node_ == b:
        result.append(cnt)
    for node in g[node_]:
        if v[node]:
            continue
        deq.append((node, cnt+1))
        v[node] = True

write(str(min(result)))
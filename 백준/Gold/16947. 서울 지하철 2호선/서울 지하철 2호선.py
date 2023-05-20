from collections import deque
from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n = int(read().rstrip())
v = [0] * (n+1)
g = [[] for _ in range(n+1)]
for _ in range(n):
    a, b = list(map(int, read().rsplit(' ')))
    g[a].append(b)
    g[b].append(a)

c_node = []

for node in range(1, n+1):
    if c_node: break
    stack = [(node, [node])]

    while stack:
        n_, history = stack.pop()
        v[n_] = node
        for nn in g[n_]:
            if (nn == node and 
                len(c_node) < len(history) and 
                len(history) > 2):
                c_node = history
            if v[nn] == node: continue
            stack.append((nn, history+[nn]))

v = [0] * (n+1)
result = []
for node in range(1, n+1):
    stack = [(node, 0)]
    v[node] = node

    while stack:
        n_, cnt = stack.pop()
        if n_ in c_node:
            result.append(cnt)
            break
        for nn in g[n_]:
            if v[nn] == node: continue
            v[nn] = node
            stack.append((nn, cnt+1))

write(' '.join(list(map(str, result))))
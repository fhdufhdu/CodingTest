from collections import deque
from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n = int(read().rstrip())
g = [deque([]) for _ in range(n+1)]
v = [False] * (n+1)
for _ in range(n-1):
    a, b = list(map(int, read().rsplit(' ')))
    g[a].append(b)
    g[b].append(a)
o = list(map(int, read().rsplit(' ')))
comp = [0] * (n+1)


for i in range(n):
    comp[o[i]] = i
for i in range(n+1):
    g[i] = sorted(g[i], key=lambda x:comp[x])

history = []
def dfs(x:int):
    history.append(x)
    for nn in g[x]:
        if v[nn]: continue
        v[nn] = True
        dfs(nn)

v[1] = True
dfs(1)

if history == o:
    write('1')
else:
    write('0')
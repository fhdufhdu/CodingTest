"""input
3
1.0 1.0
2.0 2.0
2.0 4.0
"""
from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n = int(read().rstrip())
coord = []
for _ in range(n):
    a, b = list(map(float, read().rstrip().split(' ')))
    coord.append((a, b))

g = []
for i in range(n):
    for j in range(n):
        if i <= j: continue
        x1, y1 = coord[i]
        x2, y2 = coord[j]
        weight = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
        g.append((i, j, weight))

g = sorted(g, key=lambda x:x[2])
set_arr = [ i for i in range(n)]

def find(a):
    pre = []
    while set_arr[a] != a:
        pre.append(a)
        a = set_arr[a]
    for p in pre:
        set_arr[p] = a
    return a

def union(a, b):
    ar = find(a)
    br = find(b)
    set_arr[ar] = br

result = 0
for a, b, weight in g:
    if find(a) == find(b): continue
    result += weight
    union(a, b)

write(f'{result}\n')
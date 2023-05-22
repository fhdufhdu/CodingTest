from collections import deque
from sys import stdin, stdout

read = stdin.readline
write = stdout.write


data = list(map(int, read().rsplit( )))
v = [[False] * 1600 for _ in range(1600)]
deq = deque([])

a, b = data[0], data[1]

if a > b: a, b = b, a
deq.append((a, b))
v[a][b]=True

total = sum(data)
if total % 3 != 0:
    write('0')
    exit()

while deq:
    a, b = deq.popleft()
    c = total - a - b
    if a == b == c:
        write('1')
        exit()
        
    for aa, bb in (a, b), (b, c), (a, c):
        if aa == bb: continue
        if bb < aa: aa, bb = bb, aa
        bb -= aa    
        aa += aa
        cc = total - aa - bb

        na = min(aa, bb, cc)
        nb = max(aa, bb, cc)

        if v[na][nb]: continue

        v[na][nb] = True
        deq.append((na, nb))

write('0')
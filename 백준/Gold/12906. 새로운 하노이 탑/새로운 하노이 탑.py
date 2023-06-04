from sys import stdin, stdout
from collections import deque

read = stdin.readline
write = stdout.write

a = read().rstrip().rsplit(' ')
b = read().rstrip().rsplit(' ')
c = read().rstrip().rsplit(' ')

if len(a) == 1: a = ''
else: a = a[1].rstrip()
if len(b) == 1: b = ''
else: b = b[1].rstrip()
if len(c) == 1: c = ''
else: c = c[1].rstrip()

v = {}
deq = deque([(a, b, c, 0)])
v.setdefault(f"{a},{b},{c}", 0)

result = 0
while deq:
    aa, bb, cc, move = deq.popleft()

    acnt = 0
    for a_ in aa:
        if a_ == 'A': acnt += 1
    bcnt = 0
    for b_ in bb:
        if b_ == 'B': bcnt += 1
    ccnt = 0
    for c_ in cc:
        if c_ == 'C': ccnt += 1

    if len(aa) == acnt and len(bb) == bcnt and len(cc) == ccnt:
        result = move
        break

    for i in range(3):
        for j in range(3):
            if i == j: continue
            top = [aa, bb, cc]
            if not top[i]: continue
            iv=top[i][-1]
            top[i] = top[i][:len(top[i])-1]
            top[j] += iv

            topstr = f"{top[0]},{top[1]},{top[2]}"
            if topstr in v:
                if v[topstr] <= move+1: continue

            v.setdefault(topstr, move+1)
            deq.append((*top, move+1))

write(str(result)) 
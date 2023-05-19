from collections import deque
from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n, s = list(map(int, read().rsplit(' ')))
data = list(map(int, read().rsplit(' ')))

hn = n // 2
adata = data[:hn]
bdata = data[hn:]

sum_map = {}
def dfsa(x:int, sumv:int):
    global sum_map

    if x == hn: 
        sum_map.setdefault(sumv, 0)
        sum_map[sumv] += 1
        return

    dfsa(x+1, sumv+adata[x])
    dfsa(x+1, sumv)

cnt = 0
def dfsb(x:int, sumv:int):
    global sum_map, cnt
    if x == n-hn: 
        if (s-sumv) in sum_map:
            cnt += sum_map[s-sumv]
        return

    dfsb(x+1, sumv+bdata[x])
    dfsb(x+1, sumv)

dfsa(0, 0)
dfsb(0, 0)

if s == 0 and cnt != 0: cnt -= 1

write(str(cnt))
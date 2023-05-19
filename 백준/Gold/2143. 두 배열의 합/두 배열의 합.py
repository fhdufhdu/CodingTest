from collections import deque
from sys import stdin, stdout

read = stdin.readline
write = stdout.write

t = int(read().rstrip())
n = int(read().rstrip())
a = list(map(int, read().rsplit(' ')))
m = int(read().rstrip())
b = list(map(int, read().rsplit(' ')))


sum_map = {}
for i in range(n):
    sumv = 0
    for j in range(i, n):
        sumv += a[j]
        sum_map.setdefault(sumv, 0)
        sum_map[sumv] += 1

cnt = 0 
for i in range(m):
    sumv = 0
    for j in range(i, m):
        sumv += b[j]
        if (t - sumv) in sum_map:
            cnt += sum_map[t - sumv]

write(str(cnt))
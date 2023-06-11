from sys import stdin, stdout
from collections import deque

read = stdin.readline
write = stdout.write

n = int(read().rstrip())
data = list(map(int, read().rsplit(' ')))
m = int(read().rstrip())
qlist = [list(map(int, read().rsplit(' '))) for _ in range(m)]
ans = [[0] * n for _ in range(n)]

for i in range(n):
    cnt = 0
    for j in range(i, n):
        if data[i] == data[j]:
            ans[i][j] = 1
        else: break
    for j in range(i, -1, -1):
        other_j = i * 2 - j
        if not(0<= other_j < n): continue
        if data[j] == data[other_j]:
            ans[j][other_j] = 1
        else: break
result = []
for q in qlist:
    s, e = q
    result.append(str(ans[s-1][e-1]))

write("\n".join(result))
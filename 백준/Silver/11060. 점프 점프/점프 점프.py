from sys import stdin, stdout
from collections import deque

read = stdin.readline
write = stdout.write

n = int(read().rstrip())
data = list(map(int, read().rsplit(' ')))
ans = [10000000000] * n

ans[0] = 0
for i in range(n): 
    for j in range(1, data[i]+1):
        if i + j >= n: continue
        if ans[i + j] > ans[i] + 1:
            ans[i + j] = ans[i] + 1

if ans[-1] == 10000000000:
    ans[-1] = -1
write(str(ans[-1]))
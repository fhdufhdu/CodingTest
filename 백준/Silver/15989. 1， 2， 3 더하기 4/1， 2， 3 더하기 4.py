from sys import stdin, stdout
from collections import deque

read = stdin.readline
write = stdout.write

t = int(read().rstrip())

data = [0] * 10001
data[1] = 1
data[2] = 2
data[3] = 3
for i in range(4, 10001):
    data[i] = data[i-3] + (i//2) + 1

result = []
for _ in range(t):
    n = int(read().rstrip())
    result.append(str(data[n])) 

write("\n".join(result))
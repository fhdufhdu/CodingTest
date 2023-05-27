from sys import stdin, stdout
from collections import deque

read = stdin.readline
write = stdout.write

n, m = list(map(int, read().rsplit(' ')))
write(str(n+m))
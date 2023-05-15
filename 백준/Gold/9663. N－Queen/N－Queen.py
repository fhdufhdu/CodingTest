import copy
from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n = int(read().rstrip())
col = [0] * n
result = 0 

def check(k:int):
    for i in range(k):
        if (col[i] == col[k]) or (abs(i - k) == abs(col[i] - col[k])):
            return True
    return False

def dfs(i: int):
    global result
    if i == n:
        result += 1
        return
    for j in range(n):
        col[i] = j
        if check(i): continue
        dfs(i+1)

dfs(0)

write(str(result))
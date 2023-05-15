import copy
from sys import stdin, stdout

read = stdin.readline
write = stdout.write

data = [list(map(int, read().rstrip().rsplit(' '))) for _ in range(9)]
start_point = [(None, None)]

def dfs(i:int, j:int):
    if not start_point:
        write("\n".join([' '.join(list(map(str,r))) for r in data]))
        exit()

    gi = i // 3 
    gj = j // 3
    g_data = []
    row_data = data[i]
    col_data = [data[k][j] for k in range(9)]
    for k in range(3*gi, 3*gi + 3):
        for l in range(3*gj, 3*gj + 3):
            g_data.append(data[k][l])


    for k in range(9):
        if k+1 in row_data or k+1 in col_data or k+1 in g_data: continue
        origin = data[i][j]
        data[i][j] = k+1
        ni, nj = start_point.pop()
        dfs(ni, nj)
        start_point.append((ni, nj))
        data[i][j] = origin
    
for i in range(9):
    for j in range(9):
        if data[i][j] == 0:
            start_point.append((i, j))

i, j = start_point.pop()
dfs(i, j)
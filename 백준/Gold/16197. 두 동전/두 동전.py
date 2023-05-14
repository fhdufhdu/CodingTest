from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n, m = list(map(int, read().rsplit(' ')))
mat = [list(read().rstrip()) for _ in range(n)]
coins = []

for i in range(n):
    for j in range(m):
        if mat[i][j] == 'o':
            coins.append((i, j))

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

min_v = 10**10
def dfs(cnt:int):
    global min_v
    if cnt > 10:
        return

    cx1, cy1 = coins[0] 
    cx2, cy2 = coins[1] 
    for dx, dy in d:
        fall_cnt = 0
        ccx1 = cx1 + dx
        ccy1 = cy1 + dy
        ccx2 = cx2 + dx
        ccy2 = cy2 + dy
        if not(0 <= ccx1 < n and 0 <= ccy1 < m): 
            fall_cnt += 1
        elif mat[ccx1][ccy1] == '#':
            ccx1, ccy1 = cx1, cy1
        if not(0 <= ccx2 < n and 0 <= ccy2 < m): 
            fall_cnt += 1
        elif mat[ccx2][ccy2] == '#':
            ccx2, ccy2 = cx2, cy2

        if fall_cnt == 1:
            min_v = min(cnt, min_v)
            continue
        if fall_cnt == 2: continue
        
        coins[0] = (ccx1, ccy1)
        coins[1] = (ccx2, ccy2)
        dfs(cnt+1)
        coins[0] = (cx1, cy1)
        coins[1] = (cx2, cy2)

dfs(1)
min_v = -1 if min_v == 10**10 else min_v
write(str(min_v))
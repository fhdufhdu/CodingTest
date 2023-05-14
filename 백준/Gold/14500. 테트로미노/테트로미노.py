from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n, m = list(map(int, read().rsplit(' ')))
mat = [list(map(int, read().rsplit(' '))) for _ in range(n)]
v = [[-1] * m for _ in range(n)]


d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max = 0

def dfs(i:int, j:int, cnt:int, sum:int):
    if cnt == 4:
        global max
        if sum > max: max = sum
        return
    
    for dx, dy in d:
        x = i+dx
        y = j+dy
        if not(0<=x<n and 0<=y<m): continue
        if v[x][y] == v_std: continue

        v[x][y] = v_std
        dfs(x, y, cnt + 1, sum + mat[x][y])
        v[x][y] = v_std - 1

for i in range(n):
    for j in range(m):
        v_std = i * n + j

        v[i][j] = v_std
        dfs(i, j, 1, mat[i][j]) 
        v[i][j] = v_std - 1
         
        for k in range(4):
            sum = mat[i][j]
            for l in range(4):
                if k == l: continue   
                x = i + d[l][0]
                y = j + d[l][1]
                if not(0<=x<n and 0<=y<m):
                    sum = -1
                    break
                sum += mat[x][y]
            if sum > max:
                max = sum

write(str(max))

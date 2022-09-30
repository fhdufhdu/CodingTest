from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n, m = map(int, read().split())
mat = [[0] * (n+1)]
sum = [[0]*(n+1) for _ in range(n+1)]
for _ in range(n):
    mat_ = [0] + list(map(int, read().split()))
    mat.append(mat_)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + mat[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, read().split())
    write(f'{sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1]}\n') 
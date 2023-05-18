from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n, s = list(map(int, read().rsplit(' ')))
data = list(map(int, read().rsplit(' ')))
dp = [0] * n

sumv = 0
for i in range(n):
    sumv += data[i]
    dp[i] = sumv

minv = 2*n
for i in range(-1, n):
    for j in range(i+1, n):
        if i == -1 and dp[j] >= s:
            minv = min(minv, j+1)
            break
        elif (dp[j] - dp[i]) >= s:
            minv = min(minv, j - i)
            break
        
if minv == 2*n: minv = 0
write(str(minv))
from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n = int(read().rstrip())
data = [tuple(map(int, read().rstrip().split(' '))) for _ in range(n)]

data = sorted(data, key=lambda x:(-x[1], -x[0]))

ans = 10000000
for duration, end in data:
    ans = min(ans - duration, end - duration)
ans = -1 if ans < 0 else ans
write(str(ans))
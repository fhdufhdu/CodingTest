from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n, m = map(int, read().split())

data = list(map(int, read().split()))
data.append(-1)

p1 = p2 = 0
r = 0
cnt = 0
while p1 < n + 1:
    if r < m:
        r += data[p1]
        p1 += 1
    elif r > m:
        r -= data[p2]
        p2 += 1
    else:
        r += data[p1]
        cnt += 1
        p1 += 1

write(f'{cnt}\n')

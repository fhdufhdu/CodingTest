from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n, r1, c1, r2, c2 = list(map(int, read().rstrip().split(' ')))

data = {}
min_range = min(r1, c1, r2, c2)
max_range = max(r1, c1, r2, c2)
max_length = 2 * n - 1
for i in range(min_range, max_range + 1):
    data[i] = (int((i / max_length)) * max_length) + (n - 1)

for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        std_x, std_y = (data[i], data[j])
        dis = abs(i - std_x) + abs(j - std_y)
        if dis >= n:
            write('.')
        else:
            dis = dis % 26
            write(chr(ord('a') + dis))
    write('\n')

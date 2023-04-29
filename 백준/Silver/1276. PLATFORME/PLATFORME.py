from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n = int(read().rstrip())
data = []
for _ in range(n):
    y, x1, x2 = list(map(int, read().rsplit(' ')))
    data.append((y, x1, x2))
data = sorted(data, key=lambda x:-x[0])

cnt = 0
for y, x1, x2 in data:
    flag = False
    for y_, x1_, x2_ in data:
        if y <= y_: continue
        if x1_ <= x1 < x2_: 
            cnt += y - y_
            flag = True
            break
    if not flag:
        cnt += y
    flag = False
    for y_, x1_, x2_ in data:
        if y <= y_: continue
        if x1_ < x2 <= x2_: 
            cnt += y - y_
            flag = True
            break
    if not flag:
        cnt += y
    
write(str(cnt))
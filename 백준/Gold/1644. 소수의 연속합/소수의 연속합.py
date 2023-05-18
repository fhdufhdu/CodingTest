from sys import stdin, stdout

read = stdin.readline
write = stdout.write

max = 4000001
p = [True] * max
p[0] = False
p[1] = False

for i in range(2, int((max - 1) ** 0.5) + 1):
    if p[i] == True:
        idx = i ** 2
        while idx <= max-1:
            p[idx] = False
            idx += i

n = int(read())
p_list = []
for i in range(1, n+1):
    if p[i] == True:
        p_list.append(i)

p_list.append(0)

p1=p2=0
s = 0
cnt = 0
while p1 < len(p_list):
    if s <= n:
        if s == n:
            cnt += 1
        s += p_list[p1]
        p1 += 1
    else:
        s -= p_list[p2]
        p2 += 1

write(f'{cnt}\n')

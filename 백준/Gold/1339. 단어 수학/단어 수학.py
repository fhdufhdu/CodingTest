from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n = int(read().rstrip())
data = [list(read().rstrip()) for _ in range(n)]
alpha = [0] * 26

for d in data:
    for idx, d_ in enumerate(d):
        p = len(d) - 1 - idx
        ai = ord(d_) - ord('A')
        alpha[ai] += 10 ** p


alpha_ = []
for idx, p in enumerate(alpha):
    if p == 0: continue
    alpha_.append((idx, p))
alpha_ = sorted(alpha_, key=lambda x:-x[1])

alpha_value = {}
value = 9
for idx, p in alpha_:
    a = chr(ord('A') + idx)
    alpha_value.setdefault(a, value)
    value -= 1

sum = 0
for d in data:
    sum += int(''.join([str(alpha_value[d_]) for d_ in d]))
write(str(sum))
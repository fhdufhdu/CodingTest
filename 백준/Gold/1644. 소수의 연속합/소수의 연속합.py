from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n = int(read().rstrip())

prime_net = [True] * 4000001
prime_net[0] = False
prime_net[1] = False

prime_list = []
for i in range(2, int(4000000 ** 0.5) + 1):
    if not prime_net[i]: continue
    ni = i ** 2
    while ni < 4000001:
        prime_net[ni] = False
        ni += i

for i in range(2, n+1):
    if prime_net[i]:
        prime_list.append(i)

prime_list.append(0)

p1 = p2 = 0
cnt = 0
sumv = 0

while p1 < len(prime_list):
    if sumv <= n:
        if sumv == n:
            cnt += 1
        sumv += prime_list[p1]
        p1 += 1
    else:
        sumv -= prime_list[p2]
        p2 += 1

write(str(cnt))
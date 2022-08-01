from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n, m = map(int, read().split())
n_list = list(map(int, read().split()))
n_list = [0] + n_list

sum = 0

for i in range(len(n_list)):
    sum += n_list[i]
    n_list[i] = sum

for _ in range(m):
    i, j = map(int, read().split())
    write(f'{n_list[j] - n_list[i-1]}\n')

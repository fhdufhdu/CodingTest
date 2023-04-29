from sys import stdin, stdout
import time
read = stdin.readline
write = stdout.write

n, m = list(map(int, read().rsplit(' ')))
a_list = [list(read().rstrip()) for _ in range(n)]
a_list = [a*2 for a in a_list]
a_list *= 2

result = [0 for _ in range(26)]
for i in range(2*n):
    t = (i + 1)*(2*n - i)
    for j in range(2*m):
        r = (j + 1)*(2*m - j)
        result[ord(a_list[i][j]) - ord('A')] += t*r

write("\n".join([str(r) for r in result]))

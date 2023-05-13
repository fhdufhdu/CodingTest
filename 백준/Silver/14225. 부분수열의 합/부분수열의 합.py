from sys import stdin, stdout

read = stdin.readline
write = stdout.write

n = int(read().rstrip())
s = list(map(int, read().rsplit(' ')))

sum_set = set()
def sum_(idx:int, sum_v:int):
    sum_set.add(sum_v)
    if idx >= len(s) - 1:
        return
    
    for i in range(idx+1, len(s)):
        sum_(i, sum_v + s[i])

for i in range(len(s)):
    sum_(i, s[i])

sum_list = sorted(list(sum_set))

for i in range(2000000):
    if i >= len(sum_list):
        break
    elif i + 1 != sum_list[i]:
        break

write(str(i+1))
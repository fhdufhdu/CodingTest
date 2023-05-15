from sys import stdin, stdout

read = stdin.readline
write = stdout.write

k = int(read().rstrip())
data = list(read().rstrip().rsplit(' '))
v = [False for i in range(10)]
min_v = "999"
max_v = "000"

def dfs(depth:int, history:list):
    global min_v, max_v
    if depth == k:
        history_str = "".join(list(map(str, history)))
        min_v = min(min_v, history_str)
        max_v = max(max_v, history_str)
        return

    for nnum in range(10):
        if v[nnum]: continue

        if (data[depth] == '<' and history[-1] < nnum) or (data[depth] == '>' and history[-1] > nnum):
            v[nnum] = True
            dfs(depth+1, history + [nnum])
            v[nnum] = False

for i in range(10):
    v[i] = True
    dfs(0, [i])
    v[i] = False

write(f'{max_v}\n{min_v}')
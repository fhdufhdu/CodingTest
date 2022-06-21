from sys import stdin, stdout

read = stdin.readline
write = stdout.write

N, K = list(map(int, read().rstrip().split(' ')))

visited = [False] * N
visited_cnt = 0
cur_node = 0

result = []
while visited_cnt < N:
    iter_cnt = 0
    while iter_cnt < K - 1:
        cur_node += 1
        if cur_node >= N:
            cur_node %= N
        if visited[cur_node]:
            continue
        iter_cnt += 1

    visited[cur_node] = True
    visited_cnt += 1
    result.append(cur_node + 1)
    while visited[cur_node] and visited_cnt < N:
        cur_node += 1
        if cur_node >= N:
            cur_node %= N

write(str(result).replace('[', '<').replace(']', '>'))
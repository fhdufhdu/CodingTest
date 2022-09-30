from sys import stdin, stdout
import heapq

read = stdin.readline
write = stdout.write

V, E = map(int, read().split())
V += 1
k = int(read())
g = [[] for _ in range(V)]

for i in range(E):
    u, v, w = map(int, read().split())
    g[u].append((w, v))

ans = [3000001] * V

heap = []
heapq.heappush(heap, (0, k))
ans[k] = 0

while heap:
    weight, node = heapq.heappop(heap)
    if ans[node] < weight:
        continue
    for w, v in g[node]:
        if ans[v] > weight + w:
            ans[v] = weight + w
            heapq.heappush(heap, (w+weight, v))

for i in range(1, V):
    if ans[i] == 3000001:
        write('INF\n')
    else:
        write(f'{ans[i]}\n')

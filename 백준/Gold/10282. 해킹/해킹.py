from sys import stdin, stdout
import heapq

read = stdin.readline
write = stdout.write

t = int(read())

for _ in range(t):
    n, d, c = map(int, read().split())
    n += 1
    g = [[] for _ in range(n)]
    for _ in range(d):
        a, b, s = map(int, read().split())
        g[b].append((s,a))
    
    ans = [10000 * 1000] * n
    heap = []
    heapq.heappush(heap, (0, c))
    ans[c] = 0
    last = 0
    last_w = 0

    while heap:
        weight, pos = heapq.heappop(heap)

        if ans[pos] < weight:
            continue
        for w, p in g[pos]:
            s_w = w + weight
            if ans[p] > s_w:
                ans[p] = s_w
                heapq.heappush(heap, (s_w, p))
        last += 1
        last_w = weight
    
    write(f'{last} {last_w}\n')
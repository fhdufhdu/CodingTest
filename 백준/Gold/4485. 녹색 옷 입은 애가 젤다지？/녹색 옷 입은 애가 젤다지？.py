from sys import stdin, stdout
import heapq

read = stdin.readline
write = stdout.write

cnt = 0
while True:
    cnt += 1
    n = int(read())
    if n == 0:
        break
    g = []
    for _ in range(n):
        g.append(list(map(int, read().split())))
    
    ans = [[(n ** 2)* 9 + 1] * n for _ in range(n)]

    heap = []
    heapq.heappush(heap, (g[0][0], 0, 0))

    while heap:
        weight, pos_a, pos_b = heapq.heappop(heap)
        if ans[pos_a][pos_b] < weight:
            continue
        for da, db in zip((1, 0, -1, 0), (0, 1, 0, -1)):
            da_ = da + pos_a; db_ = db + pos_b
            if not(0 <= da_ < n and 0 <= db_ < n):
                continue
            
            if ans[da_][db_] > weight + g[da_][db_]:
                ans[da_][db_] = weight + g[da_][db_]
                heapq.heappush(heap, (ans[da_][db_], da_, db_))
    
    write(f'Problem {cnt}: {ans[n-1][n-1]}\n')

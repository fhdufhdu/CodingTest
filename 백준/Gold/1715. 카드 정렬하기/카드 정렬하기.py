from sys import stdin, stdout
import heapq

read = stdin.readline
write = stdout.write

heap = []

n = int(read().rstrip())
for _ in range(n):
    value = int(read().rstrip())
    heap.append(value)

heapq.heapify(heap)

result = 0
while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a+b)
    result += a+b

write(str(result))
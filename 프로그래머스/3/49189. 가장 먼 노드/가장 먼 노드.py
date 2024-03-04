from heapq import heappop, heappush
def solution(n, edge):
    INF = int(1e9)
    answer = 0
    
    g = [[] for _ in range(n+1)]
    
    for a, b in edge:
        g[a].append(b)
        g[b].append(a)
    
    min_heap = [(0, 1)]
    
    result = [INF] * (n+1)
    
    while min_heap:
        curr_cost, curr_node = heappop(min_heap)
        if curr_cost >= result[curr_node]: continue
        result[curr_node] = curr_cost
        
        for next_node in g[curr_node]:
            heappush(min_heap, (curr_cost + 1, next_node))
    
    max_distance = max(result[1:])
    
    for i in range(1, n+1):
        if result[i] == max_distance:
            answer += 1
        
    return answer
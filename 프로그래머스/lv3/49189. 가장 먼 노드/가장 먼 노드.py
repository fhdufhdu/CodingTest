from collections import deque
def solution(n, edge):
    answer = 0 
    max_dist = 0
    g = [[] for _ in range(n+1)]
    v = [False for _ in range(n+1)] 
    for a, b in edge: 
       	g[a].append(b)
        g[b].append(a)
    
    deq = deque([(1, 0)])
    v[1] = True
    while deq:
        node, dist = deq.popleft()
        if dist > max_dist:
            max_dist = dist
            answer = 1
        elif dist == max_dist:
           	answer += 1 
        for next_node in g[node]:
            if v[next_node] :continue
            deq.append((next_node, dist + 1))
            v[next_node] = True
    return answer
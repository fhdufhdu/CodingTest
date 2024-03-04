from heapq import heappush, heappop
def solution(N, road, K):
    answer = set()
    g = [[] for _ in range(N+1)]
    v = [False] * (N+1)
    
    for a, b, cost in road:
        g[a].append((b, cost))
       	g[b].append((a, cost))
   		
    vills = [(0, 1)]
    
    while vills:
       	curr_cost, curr_vill = heappop(vills) 
        v[curr_vill] = True
        
        if curr_cost <= K:
            answer.add(curr_vill)
            
        for next_vill, next_cost in g[curr_vill]:
            if v[next_vill]: continue
            
            heappush(vills, (curr_cost+next_cost, next_vill))
        
    
    return len(answer)
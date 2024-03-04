def find(data, idx):
    prev_idx = [idx]
    while True:
        if data[idx] == idx:
            for pi in prev_idx:
                data[pi] = idx
            return idx
       	idx = data[idx]
def union(data, a, b):
    a_root = find(data, a)
    b_root = find(data, b) 
    data[b_root] = a_root
    
def solution(n, costs):
    costs = sorted(costs, key = lambda x: x[2])
    data = [i for i in range(n)]
    answer = 0
    for a, b, cost in costs:
       	if find(data, a) == find(data, b):
            continue
        union(data, a, b)
        answer += cost
        
    return answer
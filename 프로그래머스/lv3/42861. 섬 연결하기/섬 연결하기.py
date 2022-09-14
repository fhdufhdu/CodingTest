def solution(n, costs):
    answer = 0
    #최소신장트리?
    data = [i for i in range(101)]
    costs = sorted(costs, key=lambda x:x[2])
     
    def find(a):
        prev = []
       	while a != data[a]:
            prev.append(a) 
            a = data[a]
        for p in prev:
            data[p] = a
        return a
    def union(a, b):
        ar = find(a)
        br = find(b)
        data[ar] = br
    
    for a, b, cost in costs:
        if find(a) == find(b):
            continue
        union(a, b)
        answer += cost
        
    return answer
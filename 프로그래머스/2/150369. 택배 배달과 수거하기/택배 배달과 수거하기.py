def solution(cap, n, deliveries, pickups):
    answer = 0
    
    dd = [(i, d) for i, d in enumerate(deliveries)]
    pp = [(i, p) for i, p in enumerate(pickups)]
    
    while dd or pp:
        max_idx = -1
        
        curr_cap = 0
        while dd:
            i, d = dd[-1]
            if d == 0:
                dd.pop()
                continue
            max_idx = max(max_idx, i) 
            
            if curr_cap + d >= cap:
                dd[-1] = (i, d - (cap - curr_cap))
                break
            curr_cap += d
            dd.pop()
            
        curr_cap = 0
        while pp:
            i, p = pp[-1]
            if p == 0:
                pp.pop()
                continue
            max_idx = max(max_idx, i) 
            
            if curr_cap + p >= cap:
                pp[-1] = (i, p - (cap - curr_cap))
                break
            curr_cap += p
            pp.pop()
        answer += 2*(max_idx + 1)
    return answer
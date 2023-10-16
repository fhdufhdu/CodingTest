def solution(cap, n, deliveries, pickups):
    answer = 0
    
    dv = deliveries
    pu = pickups 
    
    while dv or pu:
        while dv and dv[-1] == 0: dv.pop()
        while pu and pu[-1] == 0: pu.pop()
        
        answer += 2 * max(len(dv), len(pu))
        
        curr_cap = 0
        while dv:
            d = dv.pop()
            if curr_cap + d > cap:
                dv.append(curr_cap + d - cap)
                break
            curr_cap += d
            
        curr_cap = 0
        while pu:
            p = pu.pop()
            if curr_cap + p > cap:
                pu.append(curr_cap + p - cap)
                break
            curr_cap += p
            
    return answer
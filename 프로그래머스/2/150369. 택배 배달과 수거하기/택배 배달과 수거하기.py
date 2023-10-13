def solution(cap, n, deliveries, pickups):
    answer = 0
    
    while deliveries or pickups:
        while deliveries and deliveries[-1] == 0: deliveries.pop()
        while pickups and pickups[-1] == 0: pickups.pop()
        
        answer += 2 * max(len(deliveries), len(pickups))
       	
        curr_cap = 0
        while deliveries:
            d = deliveries.pop()
            if curr_cap + d > cap:
                deliveries.append(d - (cap - curr_cap))
                break
            curr_cap += d 
            
        curr_cap = 0
        while pickups:
            p = pickups.pop()
            if curr_cap + p > cap:
                pickups.append(p - (cap - curr_cap))
                break
            curr_cap += p 
            
    return answer
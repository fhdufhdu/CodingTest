def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries or pickups:
        while deliveries and deliveries[-1] == 0: deliveries.pop()
        while pickups and pickups[-1] == 0: pickups.pop()
        
       	
        answer += 2 * max(len(deliveries), len(pickups))
        
        total_cap = 0
        while deliveries:
            curr_cap = deliveries.pop()
            if total_cap + curr_cap > cap:
                deliveries.append(curr_cap - (cap - total_cap))
                break
            total_cap += curr_cap
            
        total_cap = 0
        while pickups:
            curr_cap = pickups.pop()
            if total_cap + curr_cap > cap:
                pickups.append(curr_cap - (cap - total_cap))
                break
            total_cap += curr_cap
    return answer
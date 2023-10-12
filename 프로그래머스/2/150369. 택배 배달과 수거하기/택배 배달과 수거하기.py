def solution(cap, n, deliveries, pickups):
    answer = 0
    dd = deliveries
    pp = pickups
    
    while dd or pp:
        while dd and dd[-1] == 0: dd.pop()
        while pp and pp[-1] == 0: pp.pop()
        
        answer += 2*max(len(dd), len(pp))
        curr_d_cap = 0
        while dd:
            d = dd.pop()
            if d + curr_d_cap <= cap:
                curr_d_cap += d
            else:
                dd.append(curr_d_cap + d - cap)
                break
            
        curr_p_cap = 0
        while pp:
            p = pp.pop()
            if p + curr_p_cap <= cap:
                curr_p_cap += p
            else:
                pp.append(curr_p_cap + p - cap)
                break     
    return answer
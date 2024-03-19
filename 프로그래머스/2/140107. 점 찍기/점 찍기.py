def solution(k, d):
    answer = 0
    i = 0
    j = 0
   	
    # 0 < y**2 <= - x**2 + d**2
    
    while True:
        i_ = k * i
       	
        temp = (-(i_**2) + d ** 2) ** 0.5
        if isinstance(temp, complex):
            break 
        a = temp // k + 1
        answer += a
        if a <= 0: break
        i += 1
        
    return answer
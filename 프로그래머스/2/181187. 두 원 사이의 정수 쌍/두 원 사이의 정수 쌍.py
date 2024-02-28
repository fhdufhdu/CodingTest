import math
def solution(r1, r2):
    """
   	x^2 + y^2 = r^2 
    y^2 = r^2 - x^2
    y = sqrt(r^2 - x^2)
    """
    xy = {}
    for x in range(1, r2):
        y = int((r2**2 - x**2) ** 0.5)
        if(y == 0): continue
        
        if x < r1:
            y1 = math.ceil((r1**2 - x**2) ** 0.5)
        else: 
            y1 = 0
        
        xy[x] = y if y1 == 0 else y - y1 + 1
	
    
    answer =  ((r2 - r1) + 1) * 4 + (sum(xy.values()) * 4) 
    return answer
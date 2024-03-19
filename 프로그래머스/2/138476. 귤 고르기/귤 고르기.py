from collections import Counter

def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    
    sizes = list(counter.items())
    sizes = sorted(sizes, key=lambda x:-x[1])
	
    for size, count in sizes:
        k -= count
        answer += 1
        
        if k <= 0:
            break
            
    
    return answer
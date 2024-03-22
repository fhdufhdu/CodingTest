def k_it(n, k):
    q = n // k
    r = n % k
    if q == 0:
        return str(r)
    return f"{k_it(q, k)}{r}"

def is_prime(n):
    if n < 2: return False
	
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def solution(n, k):
    answer = 0
            
    it = k_it(n, k)
    it_list = list(map(lambda x:int(x), filter(lambda x: x!='', it.split('0'))))
   	
    for it_num in it_list:
        if is_prime(it_num):
            answer += 1
   	
    return answer
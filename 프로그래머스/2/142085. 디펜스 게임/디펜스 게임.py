from heapq import heappush, heappop
def solution(n, k, enemy):
    answer = 0

    h = []
    e_s = 0
    use = 0
    for idx, e in enumerate(enemy):
        heappush(h, (-e))
        e_s += e
        
       	if e_s > n:
            if use >= k:
                answer = idx
                break
            high_value = - heappop(h)
            e_s -= high_value
            use += 1
    if answer == 0:
        answer = len(enemy)
    return answer
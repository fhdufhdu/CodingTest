from heapq import heapify, heappush, heappop
def solution(scoville, K):
    answer = 0
    
    heapify(scoville)
   	
    while len(scoville) > 1 and scoville[0] < K:
        first = heappop(scoville)
        second = heappop(scoville)
        
        third = first + (second * 2)
        heappush(scoville, third)
        answer += 1
    if scoville[0] < K:
        answer = -1
    return answer
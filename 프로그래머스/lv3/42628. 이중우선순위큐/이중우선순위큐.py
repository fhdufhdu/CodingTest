import heapq 
def solution(operations):
    min_heap = []
    max_heap = []
    #삭제했는지 여부 확인   
    removed = [False] * 10000000
    is_min = True
    for oper in operations:
        x, y = oper.split(' ')
        y = int(y)
        if x == "I":
            heapq.heappush(min_heap, y)
            heapq.heappush(max_heap, -y)
        elif max_heap:
            if y == 1:
                data = -heapq.heappop(max_heap)     
            else:
                data = heapq.heappop(min_heap)
            removed[data] = True
        # 현재 최댓값, 최솟값이 삭제된 값이면 pop
        while max_heap:
            if not removed[-max_heap[0]]:
                break
            heapq.heappop(max_heap)
        while min_heap:
            if not removed[min_heap[0]]:
                break
            heapq.heappop(min_heap) 
    # for문 끝나고 한번 더 삭제됐는지 체크
    while max_heap:
        if not removed[-max_heap[0]]:
            break
        heapq.heappop(max_heap)
    while min_heap:
        if not removed[min_heap[0]]:
            break
        heapq.heappop(min_heap)
        
    if max_heap:
        answer = [-max_heap[0], min_heap[0]]
    else:
        answer = [0, 0]
    return answer
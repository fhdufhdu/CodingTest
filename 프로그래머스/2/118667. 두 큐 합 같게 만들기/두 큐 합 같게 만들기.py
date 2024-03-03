from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    q1_total = sum(queue1)
    q2_total = sum(queue2)
    
    MAX_CNT = 600000
    
    while q1_total != q2_total:
        if answer >= MAX_CNT:
            return -1
        if q1_total > q2_total:
            data = queue1.popleft()
            queue2.append(data)
            q1_total -= data
            q2_total += data
        else:
            data = queue2.popleft()
            queue1.append(data)
            q2_total -= data
            q1_total += data
        answer += 1
            
    return answer
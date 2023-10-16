from collections import deque
def solution(queue1, queue2):
    answer = 0
    max_answer = (len(queue1) + len(queue2)) * 2
    
    target = sum(queue1) + sum(queue2)
    if target % 2 == 1: 
        return -1
    
    target = target // 2
   	
    q1s = sum(queue1)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    while target != q1s:
        if q1s > target:
            qp = queue1.popleft() 
            q1s -= qp
            queue2.append(qp)
        else:
            qp = queue2.popleft()
            q1s += qp
            queue1.append(qp)
        answer += 1
        
        if answer > max_answer:
            return -1
    return answer
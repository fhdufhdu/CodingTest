from collections import deque
def solution(queue1, queue2):
    answer = 0
    
    q1s = sum(queue1)
    q2s = sum(queue2)
    
    max_count = len(queue1) * 3
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    while q1s != q2s:
        if q1s > q2s:
            n = q1.popleft()
            q2.append(n) 
            q1s -= n
            q2s += n
        else:
            n = q2.popleft()
            q1.append(n)
            q1s += n
            q2s -= n
        answer += 1
        if answer > max_count:
            return -1
    return answer
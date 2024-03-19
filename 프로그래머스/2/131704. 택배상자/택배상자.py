from collections import deque
def solution(order):
    answer = 0
    order = deque(order)
    stack = []
   	
    for i in range(1, len(order)+1):
        if i == order[0]:
            answer += 1
            order.popleft()
        else:
            stack.append(i)
        while stack and stack[-1] == order[0]:
            answer += 1
            order.popleft()
            stack.pop()
        
    return answer
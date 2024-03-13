def solution(numbers):
    answer = []
    
    stack = []
    
    while numbers:
        top_num = numbers.pop()
        
        while stack and stack[-1] <= top_num:
            stack.pop()
            
        if not stack:
            answer.append(-1)
        else:
            answer.append(stack[-1])
        stack.append(top_num)
    
    answer.reverse()
    return answer
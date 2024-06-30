def solution(numbers, target):
    answer = 0
	
    stack = [(0, 0)] 
    
    while stack:
        curr_value, curr_index = stack.pop()
        
        if curr_index >= len(numbers):
            if curr_value == target:
            	answer += 1
            continue
        
        for oper in ['-', '+']:
            if oper == '-':
               	next_value = curr_value - numbers[curr_index]
            else:
                next_value = curr_value + numbers[curr_index]
            stack.append((next_value, curr_index + 1))
    
    return answer
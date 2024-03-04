def solution(number, k):
    answer = ''
   	
    temp = []
    delete_count = 0
    for i in range(len(number)):
        curr_char = number[i]
        while temp:
            prev_char = temp[-1]
            if prev_char < curr_char and delete_count < k:
               	delete_count += 1 
                temp.pop()
                continue
            break
       	temp.append(curr_char)
        
    while delete_count < k:
        temp.pop()
        delete_count += 1
    return "".join(temp)
                
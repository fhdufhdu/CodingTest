from collections import deque
def compare(al, bl):
    if not al:
        return bl
        
    for i in range(len(al) - 1, -1, -1):
        if al[i] < bl[i]:
            return bl
        elif al[i] > bl[i]:
            return al
    return bl
def solution(n, info):
    answer = []
    
    queue = deque([(-1, [], n)]) 

    histories = []
    while queue:
        prev_idx, prev_history, prev_remain_arrow = queue.pop()
        
        curr_idx = prev_idx + 1
        if curr_idx >= 11:
            prev_history[10] += prev_remain_arrow
            histories.append(prev_history)
            continue
        queue.append((curr_idx, prev_history+[0], prev_remain_arrow))
        if prev_remain_arrow-info[curr_idx] >= 0:
            queue.append((curr_idx, prev_history+[info[curr_idx]], prev_remain_arrow-info[curr_idx]))
        if prev_remain_arrow-(info[curr_idx]+1) >= 0:
            queue.append((curr_idx, prev_history+[info[curr_idx]+1], prev_remain_arrow-(info[curr_idx]+1)))
        
    total_max = 0 
    for history in histories:
        appeach_total = 0
        ryan_total = 0
        for i in range(11):
            if info[i] == 0 and history[i] == 0:
                continue
            if info[i] < history[i]:
                ryan_total += 10 - i
            else:
                appeach_total += 10 - i
        
        diff_total = ryan_total - appeach_total
        if diff_total >= total_max:
            if diff_total == total_max:
                answer = compare(answer, history)
            else:
                answer = history
            total_max = diff_total
    if not answer or total_max == 0:
        answer = [-1]
    return answer
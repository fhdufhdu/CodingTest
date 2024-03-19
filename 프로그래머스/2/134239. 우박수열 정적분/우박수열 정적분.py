def solution(k, ranges):
    answer = []
    perms = [k]
    while perms[-1] != 1:
        last = perms[-1]
        if last & 1:
            next_ = last * 3 + 1
        else:
            next_ = last // 2
        perms.append(next_)
        
    areas = []
    for i in range(1, len(perms)):
        prev_y = perms[i-1]
        curr_y = perms[i]
        
        min_y, max_y = (prev_y, curr_y) if prev_y < curr_y else (curr_y, prev_y)
        
        area = ((max_y - min_y) / 2) + (min_y)
        areas.append(area)
    for a, b in ranges:
        if b <= 0:
        	b = len(perms) + b
       	if a >= b:
            answer.append(-1)
            continue
        s = sum(areas[a:b-1])
        answer.append(s)
    return answer
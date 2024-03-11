
def solution(plans):
    for idx, plan in enumerate(plans):
        h, m = plan[1].split(':')
        h, m = int(h), int(m)
        plans[idx][1] = h*60+m
        plans[idx][2] = int(plans[idx][2])
        plans[idx].append(1)
    
    plans = sorted(plans, key=lambda x: -x[1])
    curr_min = min(list(map(lambda x:x[1], plans)))
   	
    doing = []
    answer = []
    
    while doing or plans:
        if doing:
            doing_plan= doing[-1]
            if doing[-1][3] >= doing[-1][2]:
                answer.append(doing[-1][0])
                doing.pop()
            else:
                doing[-1][3] += 1
        if plans:
            top_plan = plans[-1]
            if top_plan[1] <= curr_min:
                plans.pop()
                doing.append(top_plan)
        curr_min += 1
    
    return answer
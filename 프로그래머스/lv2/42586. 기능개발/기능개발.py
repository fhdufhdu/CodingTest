def solution(progresses, speeds): 
    answer = [] 
    progresses = list(reversed(progresses))
    speeds = list(reversed(speeds))
    
    while progresses:
        progresses = [x + y for x, y in zip(progresses, speeds)] 
        pop_count = 0
        while progresses:
            top = progresses[-1]
            if top >= 100:
                progresses.pop()
                pop_count += 1
                continue
            break
       	if pop_count != 0:
            answer.append(pop_count)  
    return answer
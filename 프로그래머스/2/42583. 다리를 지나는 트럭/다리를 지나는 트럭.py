from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    not_start = deque(truck_weights)
    doing = deque([])
    
    curr_time = 0
    curr_weight = 0
    while doing or not_start:
        # 건너는 중인 트럭 확인
        while doing:
            first_truct_time, first_truct_weight = doing[0]
            if first_truct_time <= curr_time:
                curr_weight -= first_truct_weight
                doing.popleft()
            else:
                break
        # 시작하지 않은 트럭 집어넣기 
        if not_start:
            not_start_truct = not_start[0]
            if not_start_truct + curr_weight <= weight and len(doing) < bridge_length:
                not_start.popleft()
                curr_weight += not_start_truct
                doing.append((curr_time + bridge_length, not_start_truct))
        curr_time += 1
    answer = curr_time
        
    return answer
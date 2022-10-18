from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_w_d = deque(truck_weights)
    on_bridge = deque([])
    time = 0
     
    front = truck_w_d.popleft()
    on_bridge.append((front, time + bridge_length))
    left_weight = weight - front
    time += 1
    while on_bridge:
       	on_front, left_time = on_bridge[0]
       	if left_time == time:
            on_bridge.popleft()
            left_weight += on_front
        if truck_w_d:
            front = truck_w_d[0]
            if front <= left_weight:
                on_bridge.append((front, time + bridge_length))
                left_weight -= front
                truck_w_d.popleft()
        time += 1
    return time
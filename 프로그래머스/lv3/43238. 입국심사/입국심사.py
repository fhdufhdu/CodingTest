def solution(n, times):
    times = sorted(times) 
    min_time = 1
    max_time = times[-1] * n
    answer = 1000000000000000
    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        available_h = 0
        for t in times:
            available_h += (mid_time // t)
        if available_h >= n:
            if answer > mid_time:
                answer = mid_time
        if available_h < n:
           	min_time = mid_time + 1
        else:
            max_time = mid_time - 1
    return answer
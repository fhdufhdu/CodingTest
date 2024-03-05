def solution(n, times):
    """
    0~최대시간까지 구하고
    이분 탐색으로 각 분마다 가능한지 확인하기
    
    times=[7,10], n=6 이라면
    걸리는 최대 시간은 60분
    0 ~ 60분의 중간은 30분
    30분 만에 다 처리 가능한지 확인하고
    처리 가능하면 그 이전으로, 아니면 그 이후로
    """
    answer = int(1e15)
    
    times = sorted(times)
    
    min_time = 0
    max_time = times[-1] * n
    
    while min_time <= max_time:
        middle_time = min_time + ((max_time - min_time) // 2)
       	
        available_person = 0
        for time in times:
            available_person += middle_time // time
        
        if available_person >= n:
            answer = min(answer, middle_time)
            max_time = middle_time-1
        else:
            min_time = middle_time+1
        
    return answer
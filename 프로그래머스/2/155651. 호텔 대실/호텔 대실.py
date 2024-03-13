from collections import defaultdict
def solution(book_time):
    answer = 0
    b_t = []
    counter = [0] * (25*60)
   	
    for start_time, end_time in book_time:
        start_time = list(map(int, start_time.split(':')))
        end_time = list(map(int, end_time.split(':')))
        start_time = start_time[0] * 60 + start_time[1]
        end_time = end_time[0] * 60 + end_time[1] + 10
        b_t.append((start_time, end_time))
    
    b_t = sorted(b_t)
   	
    #counter = defaultdict(int)
    
    for st, et in b_t:
        for t in range(st, et):
            counter[t] += 1
    
    answer = max(counter)
    
    return answer
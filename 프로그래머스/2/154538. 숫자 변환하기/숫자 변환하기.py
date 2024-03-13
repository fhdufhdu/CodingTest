from collections import deque, defaultdict

def solution(x, y, n):
    answer = int(10e9)
    
    queue = deque([(x, 0)])

    visit = defaultdict(lambda: False)
    visit[f"{x}_{0}"] = True
    
    while queue:
        curr_x, count = queue.popleft()
        
        if curr_x == y:
            answer = min(answer, count)
            break
        
        for i in range(3):
            next_x = curr_x
            next_count = count+1
            if i == 0:
                next_x *= 3
            elif i == 1:
                next_x *= 2
            else:
                next_x += n
            if next_x > y: continue
            if visit[f"{next_x}_{next_count}"]: continue
            queue.append((next_x, count+1))
            visit[f"{next_x}_{next_count}"] = True
            
    if answer == int(10e9):
        return -1
    return answer
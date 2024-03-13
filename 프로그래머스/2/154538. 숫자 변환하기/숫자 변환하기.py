from collections import deque, defaultdict

def solution(x, y, n):
    """
    bfs로 풀어야 함.
    제일 중요한건 visit 조건 정하기임.
    """
    answer = int(10e9)
    
    queue = deque([(x, 0)])

    visit = defaultdict(lambda: int(10e9))
    visit[x] = 0
    
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
            if visit[next_x] <= next_count: continue
            queue.append((next_x, next_count))
            visit[next_x] = next_count
            
    if answer == int(10e9):
        return -1
    return answer
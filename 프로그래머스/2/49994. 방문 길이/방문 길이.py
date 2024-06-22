from collections import defaultdict
def solution(dirs):
    answer = 0
    d = {
        'U': (0, 1),
        'D': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }
    curr = (0, 0)
    visit = defaultdict(list)
    
    for _dir in dirs:
        cx, cy = curr
        dx, dy = d[_dir]
        nx, ny = cx + dx, cy + dy
        
       	if not(-5 <= nx <= 5 and -5 <= ny <=5): continue
        _next = (nx, ny)
        if not(curr in visit and _next in visit[curr]):
           	answer += 1 
       	visit[curr].append(_next)
        visit[_next].append(curr)
        curr = _next
    return answer
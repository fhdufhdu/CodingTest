from collections import deque
table = [
    [1, 1, 1],
    [5, 1, 1],
    [25, 5, 1]
]

def dfs(picks, minerals, tired):
    if picks == [0, 0, 0] or not minerals:
        return tired
    tired_list = []
    for curr_pick in range(len(picks)):
        if picks[curr_pick] < 1: continue
        
        picks[curr_pick] -= 1
       	
        got_minerals = []
        new_tired = tired
        for _ in range(5):
            if not minerals: break
            got_minerals.append(minerals.popleft())
            new_tired += table[curr_pick][got_minerals[-1]]
        
        tired_list.append(dfs(picks, minerals, new_tired))
        
        while got_minerals:
            minerals.appendleft(got_minerals.pop())
        picks[curr_pick] += 1
    return min(tired_list)
            
            
def solution(picks, minerals):
    answer = 0
    minerals = list(map(lambda x: 0 if x == 'diamond' else ( 1 if x == 'iron' else 2), minerals))
   	
    minerals = deque(minerals)
    answer = dfs(picks, minerals, 0)
    
    return answer
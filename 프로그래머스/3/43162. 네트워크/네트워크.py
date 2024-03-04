
def find(data, idx):
    prev_idx = [idx]
    while True:
        if data[idx] == idx:
            for pi in prev_idx:
                data[pi] = idx
            return idx
       	idx = data[idx]
        prev_idx.append(idx)	 

        
def union(data, a, b):
    a_root = find(data, a)
    b_root = find(data, b)
    
    for i in range(len(data)):
        if data[i] == b_root:
            data[i] = a_root
   	
def solution(n, computers):
    data = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union(data, i, j)
    return len(set(data))
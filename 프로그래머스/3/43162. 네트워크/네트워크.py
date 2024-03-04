
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
    
    """
    0 1 2라는 집합이 있을때
    1번째, 2번째를 병합하면
    0 1 1이 됨
    여기서 0번째, 2번째를 병합하면
    0 0 1이 됨
    근데 실제로는
    0 0 0이 되어야함
    그래서 아래와 같은 처리를 거치는 것
    """
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
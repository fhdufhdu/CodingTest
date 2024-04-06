def convert_idx(i, j): 
    return ((((i+1)*i) // 2) -1 ) + j

def solution(n):
    max_length = (n*(n+1)) // 2
    data = [[0]*(i+1) for i in range(n)]
    d = [(1, 0), (0, 1), (-1, -1)]
    
    stack = [(0, 0, 0, 1)]
    data[0][0] = 1
    while stack:
        i, j, p, c = stack.pop()
        if c == ((n * (n+1)) // 2):
            break
        
        di, dj = d[p]
        ni, nj = i+di, j+dj
        if not (0<=ni<n and 0<=nj<=ni) or data[ni][nj] != 0:
            p = (p+1) % 3
            stack.append((i, j, p, c))
        else:
            data[ni][nj] = c + 1
            stack.append((ni, nj, p, c+1))
    answer = []
    for d in data:
        for d_ in d:
            answer.append(d_)
    return answer
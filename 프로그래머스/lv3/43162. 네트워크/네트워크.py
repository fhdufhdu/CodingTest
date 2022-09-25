def solution(n, computers):
    answer = 0
    g = [[] for i in range(n)]
    v = [False for i in range(n)]
    for i in range(n): 
        for j in range(n):
            isConn = True if computers[i][j] == 1 else False
            if not isConn or i == j: continue
            g[i].append(j)
    for i in range(n):
        if v[i]: continue
        stack = [i]
        v[i] = True
        
        while stack:
            node = stack.pop()
            for next_node in g[node]:
                if v[next_node]: continue
                stack.append(next_node)
                v[next_node] = True
        answer += 1
    return answer
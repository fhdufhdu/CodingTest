def solution(n, wires):
    answer = 10e9
    matrix = [[[] for i in range(n+1)] for _ in range(n-1)]
    visited = [[False for i in range(n+1)] for _ in range(n-1)]
    
    for i in range(n-1):
        for j in range(n-1):
            if i == j: continue
            a, b = wires[j]
            matrix[i][a].append(b)
            matrix[i][b].append(a)
   	
    for i, g in enumerate(matrix):
        counts = []
        for j in range(1, n+1):
            if visited[i][j]: continue
            
            count = 1
            if g[j]:
                stack = [j]
                visited[i][j] = True
                while stack:
                    cnode = stack.pop()
                    for nnode in g[cnode]:
                        if visited[i][nnode]: continue

                        stack.append(nnode)
                        count += 1
                        visited[i][nnode] = True
            counts.append(count)
        answer = min(answer, abs(counts[0]-counts[1]))
    
    return answer
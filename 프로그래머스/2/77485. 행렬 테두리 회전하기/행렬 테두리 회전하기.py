from collections import deque
def solution(rows, columns, queries):
    answer = []
   	
    data = [[i*columns+j + 1 for j in range(columns)] for i in range(rows)]
    
    for si, sj, ei, ej in queries:
        si -= 1
        sj -= 1
        ei -= 1
        ej -= 1
        
        points = []
        values = deque() 
        for j in range(sj, ej+1):
            points.append((si, j))
            values.append(data[si][j])
        for i in range(si+1, ei):
            points.append((i, ej))
            values.append(data[i][ej])
        for j in range(ej, sj-1, -1):
            points.append((ei, j)) 
            values.append(data[ei][j])
        for i in range(ei-1, si, -1):
            points.append((i, sj))
            values.append(data[i][sj])
        
        values.appendleft(values.pop())
        for (i, j), v in zip(points, values):
            data[i][j] = v
        answer.append(min(values))
        
    return answer
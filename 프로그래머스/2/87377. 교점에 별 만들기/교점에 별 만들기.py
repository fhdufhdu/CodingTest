def get_cross_point(data1, data2):
    a, b, e = data1
    c, d, f = data2
   	
    adbc = a*d - b*c
    if adbc == 0:
        return None, None
    
    x = (b*f - e*d) / adbc
    y = (e*c - a*f) / adbc
    return x, y
    
def solution(line):
    answer = []
    points = set()
    for i in range(len(line)):
        for j in range(len(line)):
            if i <= j: continue
            x, y = get_cross_point(line[i], line[j])
            
            if x is None: continue
            
            if x.is_integer() and y.is_integer():
                points.add((int(x), int(y)))
    
    min_x = 10e20
    max_x = -10e20
    min_y = 10e20
    max_y = -10e20
    for x, y in points:
        min_x = min(x, min_x) 
        max_x = max(x, max_x)
        min_y = min(y, min_y)
        max_y = max(y, max_y)
    
    
    matrix = [['.']*(max_x-min_x+1) for _ in range(max_y-min_y+1)]
    for x, y in points:
        matrix[len(matrix) - 1 - (y - min_y)][x - min_x] = '*'
    
    matrix = list(map(lambda x: "".join(x), matrix))
    answer = matrix
    
    return answer
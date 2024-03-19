def solution(data, col, row_begin, row_end):
    answer = 0
    
    data = sorted(data, key=lambda x: (x[col-1], -x[0]))
    
    s_list = []
    
    for i in range(row_begin-1, row_end):
        s = 0
        for tu in data[i]:
            s += tu % (i + 1)
        s_list.append(s)
    
    answer = s_list[0]
    s_list = s_list[1:]
    
    for s in s_list:
       	answer = (answer & ~s) | (s & ~answer) 
    return answer
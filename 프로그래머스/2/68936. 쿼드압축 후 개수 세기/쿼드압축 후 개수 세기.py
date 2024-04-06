def ziparr(arr, si, sj, length):
    start_value = arr[si][sj]
    eq = True
    for i in range(si, si+length):
        for j in range(sj, sj+length):
            if start_value != arr[i][j]:
                eq = False
                break
    if eq:
        result = [0, 0]
        result[start_value] += 1
        return result
   	
    next_length = length // 2
    next_ = [
        (si, sj),
        (si+next_length, sj),
        (si, sj+next_length),
        (si+next_length, sj+next_length)
    ]
    result = [0, 0]
    for nsi, nsj in next_:
        a, b = ziparr(arr, nsi, nsj, next_length)
        result[0] += a
        result[1] += b
    return result
            
    
def solution(arr):
    answer = ziparr(arr, 0, 0, len(arr))
    return answer
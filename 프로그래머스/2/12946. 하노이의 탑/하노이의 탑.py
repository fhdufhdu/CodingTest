def hanoi(disk_num, _from, _via, _to):
    if disk_num == 1:
        return [[_from, _to]]
    result = []
    a = hanoi(disk_num-1, _from, _to, _via) 
    result.extend(a)
    result.append([_from, _to])
    b = hanoi(disk_num-1, _via, _from, _to)
    result.extend(b)
    return result
def solution(n):
    answer = hanoi(n, 1, 2, 3)
    return answer
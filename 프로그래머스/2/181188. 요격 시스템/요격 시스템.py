def solution(targets):
    targets = sorted(targets)
     
    _ranges = [targets[0]]
    
    p_f = False
    for i in range(1, len(targets)):
        a, b = targets[i]
        ra, rb = _ranges[-1]
        if ra <= a < rb:
            _ranges[-1][0] = a
            _ranges[-1][1] = min(b, rb)
        else:
            _ranges.append([a, b])
    answer = len(_ranges)

    return answer
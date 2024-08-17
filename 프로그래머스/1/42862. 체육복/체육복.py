def solution(n, lost, reserve):
    answer = 0
    lost = sorted(lost)
    reserve = sorted(reserve)
    d = {}
    for r in reserve:
        d[r] = 2
    for l in lost:
        if l in d:
            d[l] -= 1
            continue
        d[l] = 0
    for l in lost:
        prev = l-1
        next_ = l+1
        if prev in d and d[prev] >= 2:
            d[l] = 1
            d[prev] -= 1
            continue
        if next_ in d and d[next_] >= 2:
            d[l] = 1
            d[next_] -= 1
    for k, v in d.items():
        if v >= 1: answer += 1
    return answer + (n-len(d))
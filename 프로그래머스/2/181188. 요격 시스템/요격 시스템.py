def solution(targets):
    """
    1. targets을 정렬
    2. 각 target 순회하면서 겹치는 부분 계속 갱신하기
    3. 겹치는 부분없으면 answer+1하고 새롭게 겹치는 부분 생성
    4. 전체 겹치는 부분의 갯수가 정답
   	"""
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
def solution(k, d):
    """
    생각하기 빡센 문제임..
    0 < y**2 <= - x**2 + d**2
    를 구한다고 생각하면 편함.
    (- x**2 + d**2) ** 0.5가 y의 최대값임.
    거기서 점의 갯수가 최대값을 찾아서 더하면 됨
    """
    answer = 0
    i = 0
    j = 0
   	
    # 0 < y**2 <= - x**2 + d**2
    
    while True:
        i_ = k * i
       	
        temp = (-(i_**2) + d ** 2) ** 0.5
        if isinstance(temp, complex):
            break 
        a = (temp // k) + 1
        answer += a
        if a <= 0: break
        i += 1
        
    return answer
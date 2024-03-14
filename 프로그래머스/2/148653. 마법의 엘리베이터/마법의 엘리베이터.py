from collections import deque, defaultdict
def solution(storey):
    answer = 0
    sto = storey 
    while sto != 0:
        digit = sto % 10
        
        if digit <= 4:
            answer += digit
            sto -= digit
        # 245
        elif digit == 5:
            if (sto // 10) % 10 <= 4:
                answer += digit
                sto -= digit
            else:
                answer += 10-digit
                sto += 10-digit
        else:
            answer += 10-digit
            sto += 10-digit
        sto = sto // 10
        
    return answer
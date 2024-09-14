def solution(A,B):
    answer = 0
	
    A = sorted(A)
    B = sorted(B, key=lambda x: -x)
    
    for a, b in zip(A, B):
        answer += a * b

    return answer
def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a % b)
    
    
def solution(arrayA, arrayB):
    n = len(arrayA)
    answer = 0
    
    a_gcd = arrayA[0]
    for i in range(1, n):
    	a_gcd = gcd(a_gcd, arrayA[i])
    b_gcd = arrayB[0]
    for i in range(1, n):
    	b_gcd = gcd(b_gcd, arrayB[i])
   	
    if a_gcd != 1:
        not_divide = True
        for b_elem in arrayB:
            not_divide = not_divide and (b_elem % a_gcd != 0)
        if not_divide:
            answer = max(answer, a_gcd)
    if b_gcd != 1:
        not_divide = True
        for a_elem in arrayA:
            not_divide = not_divide and (a_elem % b_gcd != 0)
        if not_divide:
            answer = max(answer, b_gcd)
    
    return answer
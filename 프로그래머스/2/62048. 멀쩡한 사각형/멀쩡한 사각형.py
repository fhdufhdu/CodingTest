def gcd(a, b):
    if a > b:
        temp = a
        a = b
        b = temp
        
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
    return b

def solution(w,h):
    total = w * h
    gcd_value = gcd(w, h)
    
    w = w // gcd_value
    h = h // gcd_value
    
    answer = total - ((w + h - 1) * gcd_value)
    return answer

# https://school.programmers.co.kr/questions/64956 <- 참고해서 문제 풀었음


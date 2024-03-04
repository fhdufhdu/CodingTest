def gcd(a, b):
    while b != 0:
        temp_a = a
        a = b
        b = temp_a % b
    return a
    
def solution(a, b):
    gcd_result = gcd(a, b)
    b = b // gcd_result
    while True:
        next_b = b
        if next_b % 2 == 0:
            next_b = next_b // 2
        if next_b % 5 == 0:
            next_b = next_b // 5
        if next_b == 1:
            return 1
        elif next_b == b:
            return 2
        else:
            b = next_b
        
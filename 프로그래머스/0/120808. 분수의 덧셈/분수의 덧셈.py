def gcd(a, b):
    while b!=0:
        a,b = b, a % b
    return a
    

def solution(numer1, denom1, numer2, denom2):
    numer1 *= denom2
    numer2 *= denom1
    
    numer = numer1 + numer2
    denom = denom1 * denom2
    
    g = gcd(numer, denom)
    
    numer = int(numer / g)
    denom = int(denom / g)
    
    return [numer, denom]
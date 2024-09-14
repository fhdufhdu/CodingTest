def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def solution(arr):
    answer = 0
    while len(arr) > 1:
        a = arr.pop()
        b = arr.pop()
        lcm = (a * b) // gcd(a, b)
        arr.append(lcm)
    return arr[0]
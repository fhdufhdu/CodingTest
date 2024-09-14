def solution(s):
    numbers = list(map(lambda x: int(x), s.split(" ")))
    a = min(numbers)
    b = max(numbers)
    return f"{a} {b}"
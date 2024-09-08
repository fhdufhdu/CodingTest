def solution(n):
    """
    0 -> n으로 가는 코드보다
    n -> 0으로 가는 코드가 더 효율성이 높다
    """
    ans = 0
    while n != 0:
        if n & 1 == 0:
            n = n // 2
        else:
            n = (n - 1) // 2
            ans += 1
    return ans
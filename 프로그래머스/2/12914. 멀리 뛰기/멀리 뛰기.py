factorial = [1, 1]

for i in range(2, 2001):
    factorial.append(factorial[-1] * i)


def solution(n):
    answer = 0
    
    one_count = n
    two_count = 0
    
    while True:
        min_ = min(one_count, two_count)
        max_ = max(one_count, two_count)
        r = 1
        for i in range(max_+1, min_+max_+1):
           	r *= i
        answer = (answer + (r // factorial[min_])) % 1234567
        one_count -= 2
        two_count += 1
        if one_count < 0: break
    return answer
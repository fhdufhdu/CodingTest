from collections import deque
def calc_num(num):
    if num == 1:
        return 0
    max_ = 1
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            max_ = i
            if num // i > 10000000:
                continue
            return num // i 
    return max_
def solution(begin, end):
    answer = deque([])
    for i in range(end, begin-1, -1):
        answer.appendleft(calc_num(i))
    return list(answer)
def check(s):
    left_s = list(s)
    right_s = [left_s.pop()]
    while left_s:
        if right_s and (
            (left_s[-1] == '{' and right_s[-1] == '}') or
            (left_s[-1] == '[' and right_s[-1] == ']') or
            (left_s[-1] == '(' and right_s[-1] == ')')
        ):
            left_s.pop()
            right_s.pop()
        else:
            right_s.append(left_s.pop())
    return not right_s

from collections import deque
def solution(s):
    answer = 0
    s = deque(s)
    
    for i in range(len(s)):
        s.append(s.popleft())
        if check(s): answer += 1
    return answer
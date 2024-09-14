def solution(s):
    s = list(s)
    ts = []
    while s:
        if ts and ts[-1] == s[-1]:
            ts.pop()
            s.pop()
        else:
            ts.append(s.pop())
    return int(not (s or ts))
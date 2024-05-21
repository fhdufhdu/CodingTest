def getuv(s):
    open_count = 0
    close_count = 0
    sl = list(s)
    for idx, s_ in enumerate(s):
        if s_ == '(':
            open_count += 1
        else:
            close_count += 1
        if open_count != 0 and open_count == close_count:
            break
    u = sl[:idx+1]
    v = sl[idx+1:]
    
    return "".join(u), "".join(v)

def check_correct(s):
    count = 0
    for s_ in s:
        if s_ == '(':
            count += 1
        else:
            if count == 0:
                return False
            count += 1
    return True

def recursive(s):
    if s == "":
        return ""
    
    u, v = getuv(s)
    if check_correct(u):
        return u + recursive(v)
    else:
        result = '(' + recursive(v) + ')'
        u = list(u)[1:-1]
        u = list(map(lambda x: '(' if x==')' else ')', u))
        return result + ("".join(u))
        
        

def solution(p):
    answer = recursive(p)
    return answer
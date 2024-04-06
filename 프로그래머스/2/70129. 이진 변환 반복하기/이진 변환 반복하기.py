def digit(num):
    result = ""
    while True:
        m = num // 2
        n = num % 2
        result = str(n) + result
        if m == 0: break
       	num = m
    return result
def count(digit):
    return len(list(filter(lambda x: x=='1', list(digit))))

def solution(s):
    answer = []
    
    remove_count = 0
    convert_count = 0
    while s != '1':
        c = count(s)
        remove_count += (len(s) - c)
        s = digit(c)
        convert_count += 1
    
    answer = [convert_count, remove_count]
    return answer
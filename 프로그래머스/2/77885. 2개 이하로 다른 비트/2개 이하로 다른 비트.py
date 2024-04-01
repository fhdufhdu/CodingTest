from collections import deque
def digit(num):
    result = deque([])
    while True:
        m = num // 2
        n = num % 2
       	
        result.appendleft(n)
        
        if m == 0: break
        num = m
        
    return result

def demical(digit):
    result = 0
    for i in range(len(digit)):
        temp = digit.pop()
       	result += temp * (2 ** i)
    return result
        

def solution(numbers):
    answer = []
    for number in numbers:
        d = digit(number)
        if d[-1] == 0:
            d[-1] = 1
        else:
            d.appendleft(0)
            for i in range(1, len(d)):
                if d[-i] != d[-(i+1)]:
                    temp = d[-i]
                    d[-i] = d[-(i+1)]
                    d[-(i+1)] = temp
                    break
        answer.append(demical(d))
        
    return answer
"""
01 10
10 11
11 101
100 101
101 110
110 111
0111 1011
1000 1001
"""

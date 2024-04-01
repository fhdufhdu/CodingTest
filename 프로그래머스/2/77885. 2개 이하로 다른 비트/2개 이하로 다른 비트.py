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
수가 짝수일 때 (맨 오른쪽이 0일때) -> 맨 오른쪽을 1로 변경
수가 홀수일 때 맨 왼쪽에 0넣고, 맨 오른쪽부터 두개씩 탐색
ex) 11(01011)이 x라고 가정
01011
   ^^  => 두 값이 같음, 왼쪽으로 시프트
01011
  ^^   => 두 값이 다름, 두 값을 swap하기 => 1101 => 이 값이 정답임
"""

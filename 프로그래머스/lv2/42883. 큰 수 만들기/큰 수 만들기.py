from collections import Counter
def solution(number, k):
    answer = []
    for i in range(0,len(number)):
        cur = int(number[i])
        while answer:
            prev = int(answer[-1])
            if prev < cur and k > 0:
                answer.pop()
                k -= 1
                continue
            break
        answer.append(number[i])
    print(k)
    answer1 = []
    for i in range(0,len(answer)):
        cur = int(answer[i])
        while answer1:
            prev = int(answer1[-1])
            if prev <= cur and k > 0:
                answer1.pop()
                k -= 1
                continue
            break
        answer1.append(answer[i])
    for _ in range(k):
       	answer1.pop() 
    return ''.join(answer1)
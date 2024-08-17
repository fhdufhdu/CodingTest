def solution(number, k):
    answer = ''
    temp = []
    for i in range(len(number)):
        curr = number[i]
        while temp and k > 0:
            if temp[-1] < curr:
                temp.pop()
                k -= 1
                continue
            break 
        temp.append(curr)
    for _ in range(k):
        temp.pop()
    return "".join(temp)
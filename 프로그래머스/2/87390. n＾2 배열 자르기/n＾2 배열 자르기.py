def solution(n, left, right):
    answer = []
    
    for lr in range(left, right+1):
        i = lr // n
        j = lr - (i*n)
        
        if i >= j:
            answer.append(i+1)
        else:
            answer.append(j+1)
    return answer
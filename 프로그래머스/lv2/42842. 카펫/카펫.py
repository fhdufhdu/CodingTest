def solution(brown, yellow):
    answer = [] 
    for i in range(1, yellow + 1):
        j = int(yellow / i) 
        inner = i * j 
        outter = ((i + 2) * (j + 2)) - inner 
        if inner != yellow or outter != brown:
            continue  
        if i > j:
            answer.append(i + 2)   
            answer.append(j + 2)
        else:
            answer.append(j + 2)
            answer.append(i + 2)
        return answer
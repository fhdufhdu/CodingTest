from collections import Counter
def solution(want, number, discount):
    answer = 0
    counter_list = []
    for i in range(len(discount)-9):
        counter_list.append(Counter(discount[i:i+10]))
    
    for counter in counter_list:
        check = True
        for i in range(len(want)):
            w = want[i]
            n = number[i]
            
            check = check and (counter[w] >= n)
        if check:
            answer += 1
        
    return answer
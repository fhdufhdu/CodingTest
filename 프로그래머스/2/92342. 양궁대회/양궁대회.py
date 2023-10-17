from itertools import product

def solution(n, info):
    answer = [-1]
    info.reverse()
    
    win_results = product((True, False), repeat=11)
    max_sub_score = -1
    
    for win_result in win_results:
        ryan = [info[i] + 1 if win_result[i] else 0 for i in range(11)] 
       	ryan_arrow_sum = sum(ryan)
        
        if ryan_arrow_sum <= n:
            ryan[0] = n - ryan_arrow_sum
            
            ryan_score = sum(i for i in range(11) if win_result[i])
            apeach_score = sum(i for i in range(11) if not win_result[i] and info[i] != 0)
            
            if ryan_score <= apeach_score:
                continue
            
            sub_score = ryan_score - apeach_score
            if max_sub_score < sub_score:
                max_sub_score = sub_score
                answer = ryan
            elif max_sub_score == sub_score:
                for i in range(11):
                    if ryan[i] > answer[i]:
                        answer = ryan 
                        break
                    elif ryan[i] < answer[i]:
                        break
                
    answer.reverse()
    return answer
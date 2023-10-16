from itertools import product

def solution(n, info):
    answer = [-1]
    
    max_sub = 0
    for win_result in product([True, False], repeat = 11):
        r_info = [info[i]+1 if win_result[i] else 0 for i in range(11)]
        s = sum(r_info)
        if s <= n:
            a_s = 0
            r_s = 0
            r_info[-1] += n - s
            for i in range(11):
                if info[i] == r_info[i]: continue
               	if win_result[i]:
                    r_s += 10 - i
                else:
                    a_s += 10 - i
            if max_sub <= r_s - a_s:
                if max_sub == r_s - a_s:
                    if len(answer) == 1:
                        continue
                    for i in range(10, -1, -1):
                        if answer[i] < r_info[i]:
                            answer = r_info
                            break
                        elif answer[i] > r_info[i]:
                            break
                else:
                    answer = r_info
                            
                max_sub = r_s - a_s
    return answer

from collections import Counter
def solution(s):
    answer = []
    
    s = s[2:-2].split('},{')
    s = [s_.split(',') for s_ in s]
    s = sorted(s, key=lambda x: len(x))
   	
    dict_answer = {}
    for s_ in s:
        for s__ in s_:
            if s__ not in dict_answer:
                dict_answer[s__] = 1
                answer.append(s__)
                break
    answer = list(map(lambda x: int(x), answer))
    return answer
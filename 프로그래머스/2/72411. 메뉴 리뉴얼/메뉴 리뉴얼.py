from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
   	
    
    c_dicts = [defaultdict(int) for _ in course]
    
    for order in orders:
        for c, c_dict in zip(course, c_dicts):
            for cc in list(combinations(list(order), c)):
                c_dict["".join(sorted(cc))] += 1
                
    c_list = list(map(lambda c: sorted((c.items()), key=lambda x: (len(x[0]), -x[1])), c_dicts))
    for c in c_list:
        if not c: continue
        key, count = c[0]
        if count < 2: continue
        answer.append(key)
        for i in range(1, len(c)):
            if c[i][1] == count:
                answer.append(c[i][0])
            else:
                break
    answer = sorted(answer)
    return answer
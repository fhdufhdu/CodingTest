from itertools import combinations
from collections import defaultdict
def solution(relation):
    answer = 0
    
    rn = len(relation)
    cn = len(relation[0])
    
    column_numbers = [i for i in range(cn)]
    
    keys = []
    for i in range(cn):
        col_combi = list(combinations(column_numbers, i+1))
        for cc in col_combi:
            scc = set(cc)
            check = [key for key in keys if key < scc]
            if len(check) > 0: continue
            k_set = set()
            for r in relation:
                k = ""
                for c in cc:
                	k += r[c]
                k_set.add(k)
            if len(k_set) == rn:
                keys.append(scc)
    return len(keys)
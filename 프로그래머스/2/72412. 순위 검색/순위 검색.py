from collections import defaultdict
from itertools import product
from bisect import bisect_left, bisect_right

language = {
    'cpp':'0',
    'java': '1',
    'python':'2',
    '-': '-'
}
position = {
    'backend':'0',
    'frontend':'1',
    '-': '-'
}
career = {
    'junior':'0',
    'senior':'1',
    '-': '-'
}
soulfood = {
    'chicken':'0',
    'pizza':'1',
    '-': '-'
}
def solution(info, query):
    answer = []
    
    info = list(map(lambda x: x.split(' '), info))
    def query_split(query):
        cond, score = query.rsplit(' ', 1)
        cond = cond.split(' and ')
        
        return cond, score
    query = list(map(query_split, query))
    
    data = defaultdict(list)
    for l, p, c, s, score in info:
        keys = list(product([language[l], '-'],[position[p], '-'],[career[c], '-'],[soulfood[s], '-']))
        keys = list(map(lambda x:"".join(x), keys))
        for key in keys:
            data[key].append(int(score))
    
    for key, value in data.items():
        data[key] = sorted(value)
   	
    for (l, p, c, s), score in query:
        key = language[l] + position[p] + career[c] + soulfood[s]
        answer.append(len(data[key]) - bisect_left(data[key], int(score)))
    return answer
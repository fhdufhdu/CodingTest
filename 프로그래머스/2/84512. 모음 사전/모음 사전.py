from itertools import product
def solution(word):
    answer = 0
    _dict = []
    for i in range(5):
    	_dict.extend(list(product(list("AEIOU"), repeat=i+1)))
    _dict = list(map(lambda x:"".join(x), sorted(_dict)))
    __dict = {_dict[i]:i+1 for i in range(len(_dict))}
    answer = __dict[word]
    return answer
from itertools import product

def solution(word):
    answer = 0
    words = []
    for i in range(1, 6):
    	words += (list(map(lambda x:"".join(x), (product(list('AEIOU'), repeat=i)))))
    words = sorted(words)
    idx2word = {w: idx+1 for idx, w in enumerate(words)}
    answer = idx2word[word]
    return answer
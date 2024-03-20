from collections import Counter
def find(cards, visited, a):
    if visited[a]: return
    prev = [a]
    while not visited[a]:
        visited[a] = True
        a = cards[a]
        prev.append(a)
    for p in prev:
        cards[p] = a
        
def solution(cards):
    answer = 0
    cards = list(map(lambda x:x-1, cards))
    visited = [False] * len(cards)
    
    for i in range(len(cards)):
    	find(cards,visited,i)
    counter = Counter(cards)
    count = sorted(counter.values(), reverse=True)
   	
    if len(count) <= 1:
        answer = 0
    else:
    	answer = count[0] * count[1]
    return answer